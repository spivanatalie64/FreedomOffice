# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Executable_Executable,FREEDOMOFFICE_COM))

$(eval $(call gb_Executable_set_targettype_gui,FREEDOMOFFICE_COM,NO))

$(eval $(call gb_Executable_use_system_win32_libs,FREEDOMOFFICE_COM,\
    shell32 \
))

$(eval $(call gb_Executable_use_static_libraries,FREEDOMOFFICE_COM,\
    ooopathutils \
    winloader \
))

$(eval $(call gb_Executable_add_exception_objects,FREEDOMOFFICE_COM,\
    desktop/win32/source/officeloader/freedomoffice_com \
))

$(eval $(call gb_Executable_add_nativeres,FREEDOMOFFICE_COM,FREEDOMOFFICE/launcher))

$(eval $(call gb_Executable_add_default_nativeres,FREEDOMOFFICE_COM,$(PRODUCTNAME)))

# vim: set ts=4 sw=4 et:
