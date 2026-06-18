# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Executable_Executable,FREEDOMOFFICE_BIN))

$(eval $(call gb_Executable_set_include,FREEDOMOFFICE_BIN,\
    $$(INCLUDE) \
    -I$(SRCDIR)/desktop/source/inc \
))

$(eval $(call gb_Executable_add_defs,FREEDOMOFFICE_BIN,\
    $(if $(DISABLE_DYNLOADING),$(if $(SYSTEM_LIBXML),,-DNOTEST_xmlCleanupParser)) \
))

$(eval $(call gb_Executable_use_libraries,FREEDOMOFFICE_BIN,\
    $(if $(ENABLE_RUST_UNO),rust_uno-cpp) \
    sal \
    freedomofficeapp \
))

$(eval $(call gb_Executable_add_cobjects,FREEDOMOFFICE_BIN,\
    desktop/source/app/main \
))

ifeq ($(OS),EMSCRIPTEN)
$(call gb_LinkTarget_get_target,$(call gb_Executable_get_linktarget,FREEDOMOFFICE_BIN)) : $(gb_CustomTarget_workdir)/static/emscripten_fs_image/FREEDOMOFFICE.data.js.link

# don't sort; later can override previous settings!
$(eval $(call gb_Executable_add_prejs,FREEDOMOFFICE_BIN,$(SRCDIR)/static/emscripten/environment.js))
$(eval $(call gb_Executable_add_prejs,FREEDOMOFFICE_BIN,$(gb_CustomTarget_workdir)/static/emscripten_fs_image/FREEDOMOFFICE.data.js.link))
endif

ifeq ($(OS),WNT)

$(eval $(call gb_Executable_set_targettype_gui,FREEDOMOFFICE_BIN,NO))

$(eval $(call gb_Executable_add_nativeres,FREEDOMOFFICE_BIN,FREEDOMOFFICEBIN/officeloader))

$(eval $(call gb_Executable_add_default_nativeres,FREEDOMOFFICE_BIN,$(PRODUCTNAME)))

ifeq ($(COM),MSC)

$(eval $(call gb_Executable_add_ldflags,FREEDOMOFFICE_BIN,\
    /STACK:10000000 \
))

endif

endif

ifeq ($(OS),EMSCRIPTEN)
$(call gb_LinkTarget_get_target,$(call gb_Executable_get_linktarget,FREEDOMOFFICE_BIN)) : $(call gb_StaticLibrary_get_linktarget_target,unoembind)
$(call gb_LinkTarget_get_headers_target,$(call gb_Executable_get_linktarget,FREEDOMOFFICE_BIN)) : $(call gb_StaticLibrary_get_headers_target,unoembind)
$(call gb_LinkTarget__static_lib_dummy_depend,unoembind)

$(call gb_Executable_get_linktarget_target,FREEDOMOFFICE_BIN): \
    $(gb_CustomTarget_workdir)/desktop/freedomoffice_bin-emscripten-exports/exports

$(eval $(call gb_Executable_add_ldflags,FREEDOMOFFICE_BIN,\
	-s EXPORTED_FUNCTIONS=@$(gb_CustomTarget_workdir)/desktop/freedomoffice_bin-emscripten-exports/exports -Wl$(COMMA)--whole-archive $(call gb_StaticLibrary_get_target,unoembind) -Wl$(COMMA)--no-whole-archive \
	$(if $(ENABLE_EMSCRIPTEN_PROXY_TO_PTHREAD), \
	    -sPROXY_TO_PTHREAD=1 \
	    $(if $(DISABLE_GUI),, \
	        -sOFFSCREENCANVAS_SUPPORT=1 -sOFFSCREENCANVASES_TO_PTHREAD=\#qtcanvas)) \
))
ifeq ($(ENABLE_QT6),TRUE)
$(eval $(call gb_Executable_add_ldflags,FREEDOMOFFICE_BIN, \
    -s MODULARIZE=1 \
    -s EXPORT_NAME=freedomoffice_entry \
))
endif

$(call gb_Executable_get_linktarget_target,FREEDOMOFFICE_BIN): \
    $(gb_CustomTarget_workdir)/static/unoembind/bindings_uno.js \
    $(SRCDIR)/static/emscripten/uno.js \
    $(EMSCRIPTEN_EXTRA_SOFFICE_PRE_JS)

$(eval $(call gb_Executable_add_prejs,FREEDOMOFFICE_BIN,$(SRCDIR)/static/emscripten/script.js))

$(eval $(call gb_Executable_add_ldflags,FREEDOMOFFICE_BIN, \
    --post-js $(gb_CustomTarget_workdir)/static/unoembind/bindings_uno.js \
    --post-js $(SRCDIR)/static/emscripten/uno.js \
    $(foreach i,$(EMSCRIPTEN_EXTRA_SOFFICE_PRE_JS),--pre-js $(i)) \
))

ifeq ($(ENABLE_EMBINDTEST_UNO)-$(gb_SUPPRESS_TESTS),TRUE-)

$(call gb_Executable_get_linktarget_target,FREEDOMOFFICE_BIN): \
    $(SRCDIR)/unotest/source/embindtest/embindtest.js

$(eval $(call gb_Executable_add_ldflags,FREEDOMOFFICE_BIN, \
    --post-js $(SRCDIR)/unotest/source/embindtest/embindtest.js \
))

endif

endif

# vim: set ts=4 sw=4 et:
