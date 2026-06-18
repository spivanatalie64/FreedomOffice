# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Executable_Executable,FREEDOMOFFICE_EXE))

$(eval $(call gb_Executable_set_targettype_gui,FREEDOMOFFICE_EXE,YES))

$(eval $(call gb_Executable_use_system_win32_libs,FREEDOMOFFICE_EXE,\
    shell32 \
))

$(eval $(call gb_Executable_use_static_libraries,FREEDOMOFFICE_EXE,\
    ooopathutils \
    winloader \
))

$(eval $(call gb_Executable_add_exception_objects,FREEDOMOFFICE_EXE,\
    desktop/win32/source/officeloader/freedomoffice_exe \
))

$(eval $(call gb_Executable_add_nativeres,FREEDOMOFFICE_EXE,FREEDOMOFFICE/launcher))

$(eval $(call gb_Executable_add_default_nativeres,FREEDOMOFFICE_EXE,$(PRODUCTNAME)))

# vim: set ts=4 sw=4 et:
