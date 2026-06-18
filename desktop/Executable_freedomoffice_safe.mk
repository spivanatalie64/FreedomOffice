# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Executable_Executable,FREEDOMOFFICE_SAFE))

$(eval $(call gb_Executable_set_targettype_gui,FREEDOMOFFICE_SAFE,YES))

$(eval $(call gb_Executable_add_ldflags,FREEDOMOFFICE_SAFE,\
    /ENTRY:wWinMainCRTStartup \
))

$(eval $(call gb_Executable_use_static_libraries,FREEDOMOFFICE_SAFE,\
    winlauncher \
))

$(eval $(call gb_Executable_add_exception_objects,FREEDOMOFFICE_SAFE,\
    desktop/win32/source/applauncher/freedomoffice_safe \
))

$(eval $(call gb_Executable_add_nativeres,FREEDOMOFFICE_SAFE,FREEDOMOFFICE/launcher))

$(eval $(call gb_Executable_add_default_nativeres,FREEDOMOFFICE_SAFE,$(PRODUCTNAME)))

# vim: set ts=4 sw=4 et:
