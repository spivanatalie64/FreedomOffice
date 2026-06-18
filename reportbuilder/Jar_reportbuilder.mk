# -*- Mode: makefile-gmake; tab-width: 4; indent-tabs-mode: t -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

$(eval $(call gb_Jar_Jar,reportbuilder))

$(eval $(call gb_Jar_use_jars,reportbuilder,\
	java_uno \
	freedomoffice \
))

$(eval $(call gb_Jar_use_externals,reportbuilder,\
	flow-engine \
	flute \
	libbase \
	libfonts \
	libformula \
	liblayout \
	libloader \
	librepository \
	libserializer \
	libxml \
	sac \
))

$(eval $(call gb_Jar_set_manifest,reportbuilder,$(SRCDIR)/reportbuilder/java/manifest.mf))

$(eval $(call gb_Jar_set_componentfile,reportbuilder,reportbuilder/java/reportbuilder,OOO,services))

$(eval $(call gb_Jar_set_packageroot,reportbuilder,org))

$(eval $(call gb_Jar_add_sourcefiles,reportbuilder,\
    reportbuilder/java/org/freedomoffice/report/DataRow \
    reportbuilder/java/org/freedomoffice/report/DataSource \
    reportbuilder/java/org/freedomoffice/report/DataSourceException \
    reportbuilder/java/org/freedomoffice/report/DataSourceFactory \
    reportbuilder/java/org/freedomoffice/report/ImageService \
    reportbuilder/java/org/freedomoffice/report/InputRepository \
    reportbuilder/java/org/freedomoffice/report/JobDefinitionException \
    reportbuilder/java/org/freedomoffice/report/JobProperties \
    reportbuilder/java/org/freedomoffice/report/OfficeToken \
    reportbuilder/java/org/freedomoffice/report/OutputRepository \
    reportbuilder/java/org/freedomoffice/report/ParameterMap \
    reportbuilder/java/org/freedomoffice/report/ReportEngineMetaData \
    reportbuilder/java/org/freedomoffice/report/ReportEngineParameterNames \
    reportbuilder/java/org/freedomoffice/report/ReportExecutionException \
    reportbuilder/java/org/freedomoffice/report/ReportJob \
    reportbuilder/java/org/freedomoffice/report/ReportJobDefinition \
    reportbuilder/java/org/freedomoffice/report/ReportJobFactory \
    reportbuilder/java/org/freedomoffice/report/SDBCReportData \
    reportbuilder/java/org/freedomoffice/report/SDBCReportDataFactory \
    reportbuilder/java/org/freedomoffice/report/SOImageService \
    reportbuilder/java/org/freedomoffice/report/StorageRepository \
    reportbuilder/java/org/freedomoffice/report/function/metadata/AuthorFunction \
    reportbuilder/java/org/freedomoffice/report/function/metadata/AuthorFunctionDescription \
    reportbuilder/java/org/freedomoffice/report/function/metadata/MetaDataFunctionCategory \
    reportbuilder/java/org/freedomoffice/report/function/metadata/TitleFunction \
    reportbuilder/java/org/freedomoffice/report/function/metadata/TitleFunctionDescription \
    reportbuilder/java/org/freedomoffice/report/pentaho/DefaultNameGenerator \
    reportbuilder/java/org/freedomoffice/report/pentaho/OfficeNamespaces \
    reportbuilder/java/org/freedomoffice/report/pentaho/PentahoFormulaContext \
    reportbuilder/java/org/freedomoffice/report/pentaho/PentahoReportEngine \
    reportbuilder/java/org/freedomoffice/report/pentaho/PentahoReportEngineMetaData \
    reportbuilder/java/org/freedomoffice/report/pentaho/PentahoReportJob \
    reportbuilder/java/org/freedomoffice/report/pentaho/SOFormulaOpCodeMapper \
    reportbuilder/java/org/freedomoffice/report/pentaho/SOFormulaParser \
    reportbuilder/java/org/freedomoffice/report/pentaho/SOFunctionManager \
    reportbuilder/java/org/freedomoffice/report/pentaho/SOReportJobFactory \
    reportbuilder/java/org/freedomoffice/report/pentaho/StarFunctionCategory \
    reportbuilder/java/org/freedomoffice/report/pentaho/StarFunctionDescription \
    reportbuilder/java/org/freedomoffice/report/pentaho/StarReportData \
    reportbuilder/java/org/freedomoffice/report/pentaho/StarReportDataFactory \
    reportbuilder/java/org/freedomoffice/report/pentaho/StarReportModule \
    reportbuilder/java/org/freedomoffice/report/pentaho/expressions/SumExpression \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/AbstractReportElementLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/FixedTextLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/FormatValueUtility \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/FormattedTextLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/ImageElementContext \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/ImageElementLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/ObjectOleLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeDetailLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeGroupInstanceSectionLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeGroupLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeGroupSectionLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficePageSectionLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeRepeatingStructureLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeReportLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeTableLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/OfficeTableTemplateLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/TableCellLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/VariablesCollection \
    reportbuilder/java/org/freedomoffice/report/pentaho/layoutprocessor/VariablesDeclarationLayoutController \
    reportbuilder/java/org/freedomoffice/report/pentaho/loader/InputRepositoryLoader \
    reportbuilder/java/org/freedomoffice/report/pentaho/loader/InputRepositoryResourceData \
    reportbuilder/java/org/freedomoffice/report/pentaho/loader/InputResourceKey \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/DataStyle \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/FixedTextElement \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/FontFaceDeclsSection \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/FontFaceElement \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/FormatCondition \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/FormattedTextElement \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/ImageElement \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/ObjectOleElement \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeDetailSection \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeDocument \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeGroup \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeGroupInstanceSection \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeGroupSection \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeMasterPage \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeMasterStyles \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeReport \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeStyle \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeStyles \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeStylesCollection \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/OfficeTableSection \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/PageLayout \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/PageSection \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/RawText \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/ReportElement \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/TableCellElement \
    reportbuilder/java/org/freedomoffice/report/pentaho/model/VariablesDeclarationSection \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/ImageProducer \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/OfficeDocumentReportTarget \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/OleProducer \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/StyleUtilities \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/StylesWriter \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/chart/ChartRawReportProcessor \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/chart/ChartRawReportTarget \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/spreadsheet/SpreadsheetRawReportProcessor \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/spreadsheet/SpreadsheetRawReportTarget \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/text/MasterPageFactory \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/text/PageBreakDefinition \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/text/PageContext \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/text/TextRawReportProcessor \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/text/TextRawReportTarget \
    reportbuilder/java/org/freedomoffice/report/pentaho/output/text/VariablesDeclarations \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/ElementReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/OfficeDocumentXmlResourceFactory \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/OfficeStylesXmlResourceFactory \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/StarStyleXmlFactoryModule \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/StarXmlFactoryModule \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/chart/ChartReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/data/DataStyleReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/draw/ObjectOleReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/office/BodyReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/office/DocumentContentReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/office/DocumentStylesReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/office/FontFaceDeclsReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/office/MasterStylesReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/ConditionalPrintExpressionReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/DetailRootTableReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/FixedContentReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/FormatConditionReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/FormattedTextReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/FunctionReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/GroupReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/GroupSectionReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/ImageReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/MasterDetailReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/ReportElementReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/ReportReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/RootTableReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/rpt/SubDocumentReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/style/FontFaceReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/style/MasterPageReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/style/OfficeStyleReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/style/OfficeStylesReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/style/PageLayoutReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/style/StyleDefinitionReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/table/CoveredCellReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/table/TableCellReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/table/TableColumnReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/table/TableColumnsReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/table/TableReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/table/TableRowReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/table/TableRowsReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/text/NoCDATATextContentReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/text/TextContentReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/parser/xlink/XLinkReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/LengthCalculator \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/StyleMapper \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/StyleMapperKey \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/StyleMapperXmlFactoryModule \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/StyleMapperXmlResourceFactory \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/StyleMappingDocumentReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/StyleMappingReadHandler \
    reportbuilder/java/org/freedomoffice/report/pentaho/styles/StyleMappingRule \
    reportbuilder/java/org/freedomoffice/report/util/DefaultJobProperties \
    reportbuilder/java/org/freedomoffice/report/util/DefaultParameterMap \
    reportbuilder/java/org/freedomoffice/report/util/DefaultReportJobDefinition \
))

$(eval $(call gb_Jar_add_packagefiles,reportbuilder,,\
	$(SRCDIR)/reportbuilder/java/jfreereport.properties \
	$(SRCDIR)/reportbuilder/java/libformula.properties \
	$(SRCDIR)/reportbuilder/java/loader.properties \
))

$(eval $(call gb_Jar_add_packagefiles,reportbuilder,org/freedomoffice/report/function/metadata,\
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/function/metadata/Author-Function.properties \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/function/metadata/Author-Function_en_US.properties \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/function/metadata/Title-Function.properties \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/function/metadata/Title-Function_en_US.properties \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/function/metadata/category.properties \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/function/metadata/category_en_US.properties \
))

$(eval $(call gb_Jar_add_packagefiles,reportbuilder,org/freedomoffice/report/pentaho,\
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/configuration.properties \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/module.properties \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/oasis-datastyle.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/oasis-draw.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/oasis-form.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/oasis-style.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/oasis-table.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/oasis-text.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/smil.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/star-office.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/star-report.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/star-rpt.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/svg.css \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/xsl-fo.css \
))

$(eval $(call gb_Jar_add_packagefiles,reportbuilder,org/freedomoffice/report/pentaho/styles,\
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/styles/stylemapper.xml \
	$(SRCDIR)/reportbuilder/java/org/freedomoffice/report/pentaho/styles/stylemapper.xsd \
))

# vim: set shiftwidth=4 tabstop=4 noexpandtab:
