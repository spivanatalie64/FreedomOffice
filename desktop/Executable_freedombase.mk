# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Executable_Executable,FREEDOMBASE))

$(eval $(call gb_Executable_set_targettype_gui,FREEDOMBASE,YES))

$(eval $(call gb_Executable_add_ldflags,FREEDOMBASE,\
    /ENTRY:wWinMainCRTStartup \
))

$(eval $(call gb_Executable_use_static_libraries,FREEDOMBASE,\
    winlauncher \
))

$(eval $(call gb_Executable_add_exception_objects,FREEDOMBASE,\
    desktop/win32/source/applauncher/freedombase \
))

$(eval $(call gb_Executable_add_nativeres,FREEDOMBASE,FREEDOMBASE/launcher))

$(eval $(call gb_Executable_add_default_nativeres,FREEDOMBASE,$(PRODUCTNAME) Base))

# vim: set ts=4 sw=4 et:
