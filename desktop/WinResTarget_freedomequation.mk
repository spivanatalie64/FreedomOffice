# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_WinResTarget_WinResTarget,FREEDOMEQUATION/launcher))

$(eval $(call gb_WinResTarget_set_include,FREEDOMEQUATION/launcher,\
    $$(INCLUDE) \
    -I$(SRCDIR)/sysui/desktop \
))

$(eval $(call gb_WinResTarget_add_defs,FREEDOMEQUATION/launcher,\
    -DRES_APP_ICON=icons/math_app.ico \
))

$(eval $(call gb_WinResTarget_add_dependencies,FREEDOMEQUATION/launcher,\
    sysui/desktop/icons/math_app.ico \
))

$(eval $(call gb_WinResTarget_set_rcfile,FREEDOMEQUATION/launcher,desktop/win32/source/applauncher/launcher))

# vim: set ts=4 sw=4 et:
