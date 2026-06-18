# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_CppunitTest_CppunitTest,freedomofficekit_checkapi))

$(eval $(call gb_CppunitTest_add_cxxflags,freedomofficekit_checkapi, \
    $(gb_CXX03FLAGS) \
))

$(eval $(call gb_CppunitTest_add_exception_objects,freedomofficekit_checkapi, \
    freedomofficekit/qa/unit/checkapi \
))
$(eval $(call gb_CppunitTest_add_cobjects,freedomofficekit_checkapi,\
	freedomofficekit/qa/unit/compile_test \
))

$(eval $(call gb_CppunitTest_set_external_code,freedomofficekit_checkapi))

ifeq ($(OS),LINUX)
$(eval $(call gb_CppunitTest_add_libs,freedomofficekit_checkapi, \
    -ldl \
))
endif

# vim: set noet sw=4 ts=4:
