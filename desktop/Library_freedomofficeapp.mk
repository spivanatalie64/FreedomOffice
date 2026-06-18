# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Library_Library,freedomofficeapp))

$(eval $(call gb_Library_set_include,freedomofficeapp,\
    $$(INCLUDE) \
    -I$(SRCDIR)/desktop/inc \
    -I$(SRCDIR)/desktop/source/inc \
    -I$(SRCDIR)/desktop/source/deployment/inc \
))

$(eval $(call gb_Library_use_externals,freedomofficeapp, \
    icu_headers \
    icui18n \
    icuuc \
    $(if $(filter OPENCL,$(BUILD_TYPE)),clew) \
    boost_headers \
    dbus \
    $(if $(ENABLE_CURL), \
    $(if $(filter-out EMSCRIPTEN iOS,$(OS)), \
        curl \
    ))\
        orcus-parser \
        orcus )\
))

$(eval $(call gb_Library_use_custom_headers,freedomofficeapp,\
	officecfg/registry \
))

ifeq ($(OS),EMSCRIPTEN)
$(eval $(call gb_Library_use_custom_headers,freedomofficeapp, \
    static/unoembind \
))
endif

$(eval $(call gb_Library_use_api,freedomofficeapp,\
	udkapi \
	offapi \
))

$(eval $(call gb_Library_add_defs,freedomofficeapp,\
    -DDESKTOP_DLLIMPLEMENTATION \
    $(if $(filter WNT,$(OS)),-DENABLE_QUICKSTART_APPLET) \
    $(if $(filter MACOSX,$(OS)),-DENABLE_QUICKSTART_APPLET) \
))

$(eval $(call gb_Library_set_precompiled_header,freedomofficeapp,desktop/inc/pch/precompiled_freedomofficeapp))

$(eval $(call gb_Library_use_libraries,freedomofficeapp,\
    comphelper \
    cppu \
    cppuhelper \
    deploymentmisc \
    editeng \
    fwk \
    i18nlangtag \
    $(if $(filter OPENCL,$(BUILD_TYPE)),opencl) \
    sal \
    salhelper \
    sb \
    sfx \
    svl \
    svx \
    svxcore \
    svt \
    tk \
    tl \
    ucbhelper \
    utl \
    vcl \
))

ifeq ($(OS),WNT)
$(eval $(call gb_Library_use_static_libraries,freedomofficeapp,\
        windows_process )\
))
endif

ifeq ($(OS),MACOSX)

$(eval $(call gb_Library_add_cxxflags,freedomofficeapp,\
    $(gb_OBJCXXFLAGS) \
))

$(eval $(call gb_Library_use_system_darwin_frameworks,freedomofficeapp,\
    Foundation \
))

endif

ifeq ($(OS),iOS)

$(eval $(call gb_Library_add_cflags,freedomofficeapp,\
    $(gb_OBJCFLAGS) \
))

$(eval $(call gb_Library_add_cxxflags,freedomofficeapp,\
    $(gb_OBJCXXFLAGS) \
))

endif

$(eval $(call gb_Library_add_exception_objects,freedomofficeapp,\
    desktop/source/app/app \
    desktop/source/app/appinit \
    desktop/source/app/check_ext_deps \
    desktop/source/app/cmdlineargs \
    desktop/source/app/cmdlinehelp \
    desktop/source/app/desktopcontext \
    desktop/source/app/dispatchwatcher \
    desktop/source/app/initjsunoscripting \
    desktop/source/app/langselect \
    desktop/source/app/lockfile2 \
    desktop/source/app/officeipcthread \
    desktop/source/app/opencl \
    desktop/source/app/sofficemain \
        desktop/source/app/updater )\
    desktop/source/app/userinstall \
    desktop/source/migration/migration \
))

# FreedomOfficeKit bits
ifneq ($(filter $(OS),ANDROID iOS MACOSX WNT),)
$(eval $(call gb_Library_add_exception_objects,freedomofficeapp,\
	desktop/source/lib/init \
	desktop/source/lib/lokinteractionhandler \
	desktop/source/lib/lokclipboard \
	$(if $(filter $(OS),ANDROID), \
		desktop/source/lib/lokandroid) \
))
$(eval $(call gb_Library_set_componentfile,freedomofficeapp,desktop/lokclipboard,services))
else
ifneq ($(filter TRUE,$(USING_X11) $(DISABLE_GUI))($filter EMSCRIPTEN,$(OS)),)
$(eval $(call gb_Library_add_exception_objects,freedomofficeapp,\
	desktop/source/lib/init \
	desktop/source/lib/lokinteractionhandler \
	desktop/source/lib/lokclipboard \
))
$(eval $(call gb_Library_set_componentfile,freedomofficeapp,desktop/lokclipboard,services))
endif
endif

# vim: set ts=4 sw=4 et:
