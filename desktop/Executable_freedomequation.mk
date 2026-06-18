# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Executable_Executable,FREEDOMEQUATION))

$(eval $(call gb_Executable_set_targettype_gui,FREEDOMEQUATION,YES))

$(eval $(call gb_Executable_add_ldflags,FREEDOMEQUATION,\
    /ENTRY:wWinMainCRTStartup \
))

$(eval $(call gb_Executable_use_static_libraries,FREEDOMEQUATION,\
    winlauncher \
))

$(eval $(call gb_Executable_add_exception_objects,FREEDOMEQUATION,\
    desktop/win32/source/applauncher/freedomequation \
))

$(eval $(call gb_Executable_add_nativeres,FREEDOMEQUATION,FREEDOMEQUATION/launcher))

$(eval $(call gb_Executable_add_default_nativeres,FREEDOMEQUATION,$(PRODUCTNAME) Math))

# vim: set ts=4 sw=4 et:
