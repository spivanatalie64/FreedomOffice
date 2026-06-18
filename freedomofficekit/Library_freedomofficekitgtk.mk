# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Library_Library,freedomofficekitgtk))

$(eval $(call gb_Library_use_sdk_api,freedomofficekitgtk))

$(eval $(call gb_Library_add_exception_objects,freedomofficekitgtk,\
    freedomofficekit/source/gtk/lokdocview \
    freedomofficekit/source/gtk/tilebuffer \
))

$(eval $(call gb_Library_use_externals,freedomofficekitgtk,\
    boost_headers \
))

$(eval $(call gb_Library_set_include,freedomofficekitgtk,\
    $$(INCLUDE) \
    $$(GTK3_CFLAGS) \
))

$(eval $(call gb_Library_add_libs,freedomofficekitgtk,\
    $(GTK3_LIBS) \
))

$(eval $(call gb_Library_add_defs,freedomofficekitgtk,\
	-DLOK_PATH="\"$(LIBDIR)/freedomoffice/$(LIBO_LIB_FOLDER)\"" \
	-DLOK_DOC_VIEW_IMPLEMENTATION \
))

ifeq ($(OS),$(filter LINUX %BSD SOLARIS, $(OS)))
$(eval $(call gb_Library_add_libs,freedomofficekitgtk,\
    $(UNIX_DLAPI_LIBS) -lm \
))
endif

$(eval $(call gb_Library_use_packages,freedomofficekitgtk, \
    freedomofficekit_selectionhandles \
))

# vim: set noet sw=4 ts=4:
