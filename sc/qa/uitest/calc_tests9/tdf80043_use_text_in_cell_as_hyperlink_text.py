# -*- tab-width: 4; indent-tabs-mode: nil; py-indent-offset: 4 -*-
#
# This file is part of the FreedomOffice project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

from uitest.framework import UITestCase
from freedomoffice.uno.propertyvalue import mkPropertyValues
from freedomoffice.calc.document import get_cell_by_position
from uitest.uihelper.calc import enter_text_to_cell
from uitest.uihelper.common import get_state_as_dict, select_pos

class tdf80043(UITestCase):
    def test_tdf80043_empty_cell(self):
        with self.ui_test.create_doc_in_start_center("calc") as document:
            xCalcDoc = self.xUITest.getTopFocusWindow()
            xGridWindow = xCalcDoc.getChild("grid_window")

            # Select an empty cell and insert a hyperlink
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Both fields in the hyperlink dialog should be empty
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "")
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "")

                # Insert a sample hyperlink
                xTarget.executeAction("TYPE", mkPropertyValues({"TEXT": "http://www.freedomoffice.org/"}))
                xIndication.executeAction("TYPE", mkPropertyValues({"TEXT": "FreedomOffice"}))

            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))

            # Check contents of the cell
            xCell = get_cell_by_position(document, 0, 0, 0)
            self.assertEqual(xCell.getString(), "FreedomOffice")
            xTextFields = xCell.getTextFields()
            self.assertEqual(len(xTextFields), 1)
            self.assertEqual(xTextFields[0].URL, "http://www.freedomoffice.org/")

            # Reopen hyperlink dialog and check the target and the indication of the hyperlink
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog", close_button="cancel") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Text should contain the text of the cell
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "http://www.freedomoffice.org/")
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "FreedomOffice")

    def test_tdf80043_text_cell(self):
        with self.ui_test.create_doc_in_start_center("calc") as document:
            xCalcDoc = self.xUITest.getTopFocusWindow()
            xGridWindow = xCalcDoc.getChild("grid_window")

            # Select a cell including a text and insert a hyperlink
            enter_text_to_cell(xGridWindow, "A1", "FreedomOffice")
            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Text should contain the text of the cell
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "")
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "FreedomOffice")

                # Insert a sample hyperlink
                xTarget.executeAction("TYPE", mkPropertyValues({"TEXT": "http://www.freedomoffice.org/"}))

            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))

            # Check contents of the cell
            xCell = get_cell_by_position(document, 0, 0, 0)
            self.assertEqual(xCell.getString(), "FreedomOffice")
            xTextFields = xCell.getTextFields()
            self.assertEqual(len(xTextFields), 1)
            self.assertEqual(xTextFields[0].URL, "http://www.freedomoffice.org/")

            # Reopen hyperlink dialog and check the target and the indication of the hyperlink
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog", close_button="cancel") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Text should contain the text of the cell
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "http://www.freedomoffice.org/")
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "FreedomOffice")

    def test_tdf80043_link_text_cell(self):
        with self.ui_test.create_doc_in_start_center("calc") as document:
            xCalcDoc = self.xUITest.getTopFocusWindow()
            xGridWindow = xCalcDoc.getChild("grid_window")

            # Select a cell including a text and insert a hyperlink
            enter_text_to_cell(xGridWindow, "A1", "FreedomOffice")
            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Text should contain the text of the cell
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "")
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "FreedomOffice")

                # Insert a sample hyperlink
                xTarget.executeAction("TYPE", mkPropertyValues({"TEXT": "http://www.freedomoffice.org/"}))

            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))

            # Insert an additional text without a hyperlink in the cell including a hyperlink
            self.xUITest.executeCommand(".uno:SetInputMode")
            enter_text_to_cell(xGridWindow, "A1", " Document Foundation")

            # Check contents of the cell
            xCell = get_cell_by_position(document, 0, 0, 0)
            self.assertEqual(xCell.getString(), "FreedomOffice Document Foundation")
            xTextFields = xCell.getTextFields()
            self.assertEqual(len(xTextFields), 1)
            self.assertEqual(xTextFields[0].URL, "http://www.freedomoffice.org/")

            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))

            # Reopen hyperlink dialog and check the target and the indication of the hyperlink
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Text should contain the text of the cell
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "")
                xTarget.executeAction("TYPE", mkPropertyValues({"TEXT": "https://www.freedomfoundation.org/"}))
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "FreedomOffice Document Foundation")

            # Check contents of the cell - move focus, otherwise text fields won't be updated
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xCell = get_cell_by_position(document, 0, 0, 0)
            self.assertEqual(xCell.getString(), "FreedomOffice Document Foundation")
            xTextFields = xCell.getTextFields()
            self.assertEqual(len(xTextFields), 1)
            self.assertEqual(xTextFields[0].URL, "https://www.freedomfoundation.org/")

    def test_tdf80043_link_link_cell(self):
        with self.ui_test.create_doc_in_start_center("calc") as document:
            xCalcDoc = self.xUITest.getTopFocusWindow()
            xGridWindow = xCalcDoc.getChild("grid_window")

            # Select a cell including a text and insert a hyperlink
            enter_text_to_cell(xGridWindow, "A1", "Libre")
            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Text should contain the text of the cell
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "")
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "Libre")

                # Insert a sample hyperlink
                xTarget.executeAction("TYPE", mkPropertyValues({"TEXT": "http://www.freedomoffice.org/"}))

            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))

            # Insert an additional hyperlink in the cell
            self.xUITest.executeCommand(".uno:SetInputMode")
            xGridWindow.executeAction("TYPE", mkPropertyValues({"KEYCODE": "Office Document Foundation"}))
            xGridWindow.executeAction("TYPE", mkPropertyValues({"KEYCODE": "SHIFT+CTRL+LEFT"}))
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                # Text should contain the text of the cell
                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "")
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "Foundation")

                # Insert a sample hyperlink
                xTarget.executeAction("TYPE", mkPropertyValues({"TEXT": "https://www.freedomfoundation.org/"}))

            # Check contents of the cell
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xCell = get_cell_by_position(document, 0, 0, 0)
            self.assertEqual(xCell.getString(), "FreedomOffice Document Foundation")
            xTextFields = xCell.getTextFields()
            self.assertEqual(len(xTextFields), 2)
            self.assertEqual(xTextFields[0].URL, "http://www.freedomoffice.org/")
            self.assertEqual(xTextFields[1].URL, "https://www.freedomfoundation.org/")

            # Move focus to ensure cell is not in edit mode
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A1"}))

            # Reopen hyperlink dialog and check the target and the indication of the hyperlink
            with self.ui_test.execute_dialog_through_command(".uno:HyperlinkDialog") as xDialog:
                xTab = xDialog.getChild("tabcontrol")
                select_pos(xTab, "0")

                xTarget = xDialog.getChild("target")
                self.assertEqual(get_state_as_dict(xTarget)["Text"], "")
                xTarget.executeAction("TYPE", mkPropertyValues({"TEXT": "https://wiki.freedomfoundation.org/Main_Page"}))
                xIndication = xDialog.getChild("indication")
                self.assertEqual(get_state_as_dict(xIndication)["Text"], "FreedomOffice Document Foundation")

            # Check contents of the cell - move focus, otherwise text fields won't be updated
            xGridWindow.executeAction("SELECT", mkPropertyValues({"CELL": "A2"}))
            xCell = get_cell_by_position(document, 0, 0, 0)
            self.assertEqual(xCell.getString(), "FreedomOffice Document Foundation")
            xTextFields = xCell.getTextFields()
            self.assertEqual(len(xTextFields), 1)
            self.assertEqual(xTextFields[0].URL, "https://wiki.freedomfoundation.org/Main_Page")

# vim: set shiftwidth=4 softtabstop=4 expandtab:
