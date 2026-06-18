# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Executable_Executable,FREEDOMSHOW))

$(eval $(call gb_Executable_set_targettype_gui,FREEDOMSHOW,YES))

$(eval $(call gb_Executable_add_ldflags,FREEDOMSHOW,\
    /ENTRY:wWinMainCRTStartup \
))

$(eval $(call gb_Executable_use_static_libraries,FREEDOMSHOW,\
    winlauncher \
))

$(eval $(call gb_Executable_add_exception_objects,FREEDOMSHOW,\
    desktop/win32/source/applauncher/freedomshow \
))

$(eval $(call gb_Executable_add_nativeres,FREEDOMSHOW,FREEDOMSHOW/launcher))

$(eval $(call gb_Executable_add_default_nativeres,FREEDOMSHOW,$(PRODUCTNAME) Impress))

# vim: set ts=4 sw=4 et:
