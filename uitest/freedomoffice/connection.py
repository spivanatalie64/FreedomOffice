# -*- tab-width: 4; indent-tabs-mode: nil; py-indent-offset: 4 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

import subprocess
import time
import traceback
import uuid
import os
import platform
import signal

try:
    import pyuno
    import uno
except ImportError:
    print("pyuno not found: try to set PYTHONPATH and URE_BOOTSTRAP variables", flush=True)
    print("PYTHONPATH=/installation/opt/program", flush=True)
    print("URE_BOOTSTRAP=file:///installation/opt/program/fundamentalrc", flush=True)
    raise

def signal_handler(signal_num, frame):
    signal_name = signal.Signals(signal_num).name
    #print(f'Signal handler called with signal {signal_name} ({signal_num})', flush=True)

class OfficeConnection:
    def __init__(self, args):
        self.args = args
        self.FREEDOMOFFICE = None
        self.xContext = None

    def setUp(self):
        """  Create a new connection to a FreedomOffice process

        If the connection method is path the instance will be created as a
        new subprocess. If the connection method is connect the instance tries
        to connect to an existing instance with the specified socket string """
        if platform.system() != "Windows":
            signal.signal(signal.SIGCHLD, signal_handler)
            signal.signal(signal.SIGPIPE, signal_handler)

        (method, sep, rest) = self.args["--FREEDOMOFFICE"].partition(":")
        if sep != ":":
            raise Exception("FREEDOMOFFICE parameter does not specify method")
        if method == "path":
                socket = "pipe,name=pytest" + str(uuid.uuid1())
                try:
                    userdir = self.args["--userdir"]
                except KeyError:
                    raise Exception("'path' method requires --userdir")
                if not(userdir.startswith("file://")):
                    raise Exception("--userdir must be file URL")
                self.FREEDOMOFFICE = self.bootstrap(rest, userdir, socket)
        elif method == "connect":
                socket = rest
        else:
            raise Exception("unsupported connection method: " + method)

        # connect to the FREEDOMOFFICE instance
        success = False
        try:
            self.xContext = self.connect(socket)
            success = True
        finally:
            if not success and self.FREEDOMOFFICE:
                self.FREEDOMOFFICE.terminate()
                self.FREEDOMOFFICE.wait()
                self.FREEDOMOFFICE = None

    def bootstrap(self, FREEDOMOFFICE, userdir, socket):
        """ Creates a new FreedomOffice process

        @param FREEDOMOFFICE Path to the FREEDOMOFFICE installation
        @param userdir Directory of the user profile, only one process per user
                         profile is possible
        @param socket The socket string used for the PyUNO connection """

        argv = [FREEDOMOFFICE, "--accept=" + socket + ";urp",
                "-env:UserInstallation=" + userdir,
                "--quickstart=no", "--nofirststartwizard",
                "--norestore", "--nologo"]
        if "--valgrind" in self.args:
            argv.append("--valgrind")

        if "--gdb" in self.args:
            argv.insert(0, "gdb")
            argv.insert(1, "-ex")
            argv.insert(2, "run")
            argv.insert(3, "--args")
            argv[4] = argv[4].replace("FREEDOMOFFICE", "FREEDOMOFFICE.BIN")

        env = None
        environ = dict(os.environ)
        if 'LIBO_LANG' in environ:
            env = environ
            env['LC_ALL'] = environ['LIBO_LANG']

        return subprocess.Popen(argv, env=env)

    def connect(self, socket):
        """ Tries to connect to the FreedomOffice instance through the specified socket"""
        xLocalContext = uno.getComponentContext()
        xUnoResolver = xLocalContext.ServiceManager.createInstanceWithContext(
                "com.sun.star.bridge.UnoUrlResolver", xLocalContext)
        url = "uno:" + socket + ";urp;StarOffice.ComponentContext"
        print("OfficeConnection: connecting to: " + url, flush=True)
        while True:
            if self.FREEDOMOFFICE and self.FREEDOMOFFICE.poll() is not None:
                raise Exception("FREEDOMOFFICE has stopped.")

            try:
                xContext = xUnoResolver.resolve(url)
                return xContext
            except pyuno.getClass("com.sun.star.connection.NoConnectException"):
                print("NoConnectException: sleeping...", flush=True)
                time.sleep(1)

    def tearDown(self):
        """Terminate a FreedomOffice instance created with the path connection method.

        Tries to terminate the FREEDOMOFFICE instance through the normal
        XDesktop::terminate method and waits indefinitely for the subprocess
        to terminate """

        if self.FREEDOMOFFICE:
            if self.xContext:
                try:
                    print("tearDown: calling terminate()...", flush=True)
                    xMgr = self.xContext.ServiceManager
                    xDesktop = xMgr.createInstanceWithContext(
                            "com.sun.star.frame.Desktop", self.xContext)
                    xDesktop.terminate()
                    print("...done", flush=True)
                except pyuno.getClass("com.sun.star.beans.UnknownPropertyException"):
                    print("caught while TearDown:\n", traceback.format_exc(), flush=True)
                    pass  # ignore, also means disposed
                except pyuno.getClass("com.sun.star.lang.DisposedException"):
                    print("caught while TearDown:\n", traceback.format_exc(), flush=True)
                    pass  # ignore
            else:
                self.FREEDOMOFFICE.terminate()

            ret = self.FREEDOMOFFICE.wait()
            self.xContext = None
            self.FREEDOMOFFICE = None
            if ret != 0:
                raise Exception("Exit status indicates failure: " + str(ret))

    @classmethod
    def getHelpText(cls):
        message = """
 --FREEDOMOFFICE=method:location
                   specify FREEDOMOFFICE instance to connect to
                   supported methods: 'path', 'connect'
 --userdir=URL     specify user installation directory for 'path' method
 --valgrind        pass --valgrind to FREEDOMOFFICE for 'path' method

 'location' is a pathname, not a URL. 'userdir' is a URL.
 """
        return message


class PersistentConnection:
    def __init__(self, args):
        self.args = args
        self.connection = None

    def getContext(self):
        """ Returns the XContext corresponding to the FreedomOffice instance

        This is the starting point for any PyUNO access to the FreedomOffice
        instance."""
        return self.connection.xContext

    def setUp(self):
        # don't create two connections
        if self.connection:
            return

        conn = OfficeConnection(self.args)
        conn.setUp()
        self.connection = conn

    def tearDown(self):
        if self.connection:
            try:
                self.connection.tearDown()
            finally:
                self.connection = None

    def kill(self):
        """ Kills the FreedomOffice instance if it was created through the connection

        Only works with the connection method path"""
        if self.connection and self.connection.FREEDOMOFFICE:
            self.connection.FREEDOMOFFICE.kill()

# vim: set shiftwidth=4 softtabstop=4 expandtab:
