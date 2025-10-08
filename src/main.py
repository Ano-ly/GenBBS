from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplashScreen, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QFileDialog, QTreeWidget, QTreeWidgetItem, QHeaderView, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QInputDialog, QDialog, QCheckBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter, QIcon# Re-adding QPixmap and QPainter
import resources
from src.logic.data_models import Project, CategoryHigher, CategoryLower, Element, Bar
import json
import os
from src.config import MIN_BEND_RADII, SHAPE_CODE_LENGTH_MAP, SHAPE_CODE_FORMULA_STRINGS
from src.excel_exporter import ExcelExporter
# from src.gui.settings_screen import SettingsScreen
from PySide6.QtCore import QSettings
# --- Screen Classes (will eventually be in separate files) ---

class LoadingScreenWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_loading.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

class MainMenuScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        self.loaded_ui = QUiLoader().load("assets/ui/GenBBS.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(self.loaded_ui)
        self.setLayout(layout)
        self.connect_buttons()

    def connect_buttons(self):
        new_project_button = self.loaded_ui.findChild(QPushButton, "crNewFile")
        if new_project_button:
            new_project_button.clicked.connect(self.app_window.go_to_new_project_screen)

        existing_file_button = self.loaded_ui.findChild(QPushButton, "crExistingFile")
        if existing_file_button:
            existing_file_button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open Existing Project")
        file_dialog.setNameFilter("GenBBS Project Files (*.gbbs)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            self.load_project_from_file(selected_file)

    def load_project_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                project_data = json.load(f)
            
            loaded_project = Project.from_dict(project_data)

            self.app_window.current_project = loaded_project
            self.app_window.project_modified = False
            self.app_window.current_project_file_path = file_path
            self.app_window.update_window_title(loaded_project.name) # Update window title with loaded project name
            self.app_window.go_to_category1_screen() # Navigate to the main project screen
        except json.JSONDecodeError:
            QMessageBox.warning(self, "File Error", "Selected file is not a valid JSON file or is corrupted.")
        except (KeyError, ValueError) as e:
            QMessageBox.warning(self, "File Error", f"Invalid project file format: {e}. The file does not conform to the expected project structure.")
        except FileNotFoundError:
            QMessageBox.warning(self, "File Error", "Selected file not found.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")

class NewProjectScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent  # Store reference to ApplicationWindow
        self.loaded_ui = QUiLoader().load("assets/ui/GenBBS_newprj.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(self.loaded_ui)
        self.setLayout(layout)
        self.connect_buttons()

    def connect_buttons(self):
        back_button = self.loaded_ui.findChild(QPushButton, "btnBackNewprj")
        if back_button:
            back_button.clicked.connect(self.app_window.go_to_main_menu_screen)
        
        create_button = self.loaded_ui.findChild(QPushButton, "btnCreateNewprj")
        if create_button:
            create_button.clicked.connect(self.create_project_in_memory)

    def create_project_in_memory(self):
        project_name_input = self.loaded_ui.findChild(QLineEdit, "inputNameNewprj")
        if project_name_input:
            project_name = project_name_input.text().strip() # Strip whitespace
            if project_name:
                new_project = Project(name=project_name)
                self.app_window.current_project = new_project
                self.app_window.project_modified = True
                self.app_window.current_project_file_path = None
                self.app_window.update_window_title(project_name) # Update window title with new project name
                self.app_window.go_to_category1_screen()
                project_name_input.clear()
            else:
                QMessageBox.warning(self, "Input Error", "Project name cannot be empty.")

class Category1Screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        self.loaded_ui = QUiLoader().load("assets/ui/GenBBS_catg1.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(self.loaded_ui)
        self.setLayout(layout)
        self.tree_widget = self.loaded_ui.findChild(QTreeWidget, "treeWidgetCatg1")
        self.connect_buttons()
        

        
        # #Set up tree widget display
        # if self.tree_widget:
        #     self.tree_widget.setHeaderLabels(["Project Details"])
        #     header = self.tree_widget.header()

  
    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     if self.tree_widget:
    #         header = self.tree_widget.header()
    #         total_width = self.tree_widget.viewport().width()
    #         header.resizeSection(0, int(total_width * 0.66))  # ~2/3
    #         header.resizeSection(1, int(total_width * 0.34))  # ~1/3
    def connect_buttons(self):
        self.back_button = self.loaded_ui.findChild(QPushButton, "btnBackCatg1")
        self.save_button = self.loaded_ui.findChild(QPushButton, "btnSaveCatg1")
        self.label1Catg1 = self.loaded_ui.findChild(QLabel, "label1Catg1")
        self.input_new_sub_catg1 = self.loaded_ui.findChild(QLineEdit, "inputNewSubCatg1")
        self.input_new_element_catg1 = self.loaded_ui.findChild(QLineEdit, "inputNewElementCatg1")
        self.inputElementQtCatg1 = self.loaded_ui.findChild(QLineEdit, "inputElementQtCatg1")
        self.btn_create_sub_catg1 = self.loaded_ui.findChild(QPushButton, "btnCreateSubCatg1")
        self.btn_create_element_catg1 = self.loaded_ui.findChild(QPushButton, "btnCreateElementCatg1")
        self.btn_delete_item_catg1 = self.loaded_ui.findChild(QPushButton, "btnDeleteItemCatg1")
        self.btn_export_all_excel_catg1 = self.loaded_ui.findChild(QPushButton, "btnExportCatg1")
        self.btn_edit_name_catg1 = self.loaded_ui.findChild(QPushButton, "btnEditNameCatg1")

        self.back_button.clicked.connect(self.prompt_save_project)
        self.save_button.clicked.connect(self.save_current_project)
        self.btn_create_sub_catg1.clicked.connect(self.add_new_category)      
        print("Connecting signal")  
        self.btn_create_element_catg1.clicked.connect(self.add_new_element)
        self.btn_delete_item_catg1.clicked.connect(self.delete_selected_item)
        if self.btn_export_all_excel_catg1:
            self.btn_export_all_excel_catg1.clicked.connect(self.handle_export_all_bars)
        if self.btn_edit_name_catg1:
            self.btn_edit_name_catg1.clicked.connect(self._on_edit_name_button_clicked)

    def _remove_item_from_model(self, parent_item, item_to_remove):
        if isinstance(parent_item, (Project, CategoryHigher, CategoryLower)) and hasattr(parent_item, 'children'):
            parent_item.children = [child for child in parent_item.children if child.id != item_to_remove.id]
            return True
        elif isinstance(parent_item, (Project, CategoryHigher, CategoryLower)) and hasattr(parent_item, 'categories'):
            parent_item.categories = [child for child in parent_item.categories if child != item_to_remove]
            return True
        elif isinstance(parent_item, (Project, CategoryHigher, CategoryLower)) and hasattr(parent_item, 'elements'):
            parent_item.elements = [child for child in parent_item.elements if child != item_to_remove]
            return True
        print (hasattr(parent_item, 'children'))
        print (isinstance(parent_item, (Project, CategoryHigher, CategoryLower)))
        print(str(parent_item))
        return False

    def delete_selected_item(self):
        selected_items = self.tree_widget.selectedItems()
        if not selected_items:
            return

        selected_tree_item = selected_items[0]
        selected_object = selected_tree_item.data(0, Qt.UserRole)

        if selected_object == self.app_window.current_project:
            QMessageBox.warning(self, "Cannot Delete", "Cannot delete the root project.")
            return

        reply = QMessageBox.question(self, 'Delete Item', 'Are you sure you want to delete this item?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.No:
            return

        parent_tree_item = selected_tree_item.parent()
        if parent_tree_item:
            parent_object = parent_tree_item.data(0, Qt.UserRole)
            if self._remove_item_from_model(parent_object, selected_object):
                parent_tree_item.removeChild(selected_tree_item)
                self.app_window.project_modified = True
                self._apply_settings()
                # self.update_selected_item()
            else:
                QMessageBox.warning(self, "Deletion Error", "Could not remove item from model.")
        else:
            QMessageBox.warning(self, "Deletion Error", "Cannot determine parent of selected item.")

    def setup_for_view(self):
        self.input_new_sub_catg1.clear()
        self.input_new_element_catg1.clear()
        self.label1Catg1.setText("No Item Selected")
        self.inputElementQtCatg1.clear()
        print("setting up")
        self.populate_project_tree()
        self.tree_widget.itemSelectionChanged.connect(self.update_selected_item)
        self.tree_widget.itemDoubleClicked.connect(self.handle_double_click_element)
        self.input_new_element_catg1.setEnabled(False)
        self.btn_create_element_catg1.setEnabled(False)
        self.input_new_sub_catg1.setEnabled(False)
        self.btn_create_sub_catg1.setEnabled(False)
        self.btn_delete_item_catg1.setEnabled(False)
        
    def handle_double_click_element(self):
        selected_items = self.tree_widget.selectedItems()
        if selected_items:
            selected_object = selected_items[0].data(0, Qt.UserRole)
            if selected_object:
                text_to_fill = selected_object.name
                self.label1Catg1.setText(text_to_fill.upper())
        else:
            return
        if isinstance(selected_object, Element):
            # Disable element creation when Project is selected
            print ("Is instance")
            if self.input_new_element_catg1:
                self.input_new_element_catg1.setEnabled(False)
            if self.btn_create_element_catg1:
                self.btn_create_element_catg1.setEnabled(False)
            if self.inputElementQtCatg1:
                self.inputElementQtCatg1.setEnabled(False)
            if self.input_new_sub_catg1:
                self.input_new_sub_catg1.setEnabled(False)
            if self.btn_create_sub_catg1:
                self.btn_create_sub_catg1.setEnabled(False)
            if self.btn_delete_item_catg1:
                self.btn_delete_item_catg1.setEnabled(True)
            self.app_window.show_reinforcement_screen(selected_object)
        
    def update_selected_item(self):
        selected_items = self.tree_widget.selectedItems()
        if selected_items:
            selected_object = selected_items[0].data(0, Qt.UserRole)
            if selected_object:
                text_to_fill = selected_object.name
                self.label1Catg1.setText(text_to_fill.upper())
        else:
            return

        if isinstance(selected_object, Project):
            # Disable element creation when Project is selected
            print ("Is instance")
            if self.input_new_element_catg1:
                self.input_new_element_catg1.setEnabled(False)
            if self.btn_create_element_catg1:
                self.btn_create_element_catg1.setEnabled(False)
            if self.inputElementQtCatg1:
                self.inputElementQtCatg1.setEnabled(False)
            if self.input_new_sub_catg1:
                self.input_new_sub_catg1.setEnabled(True)
            if self.btn_create_sub_catg1:
                self.btn_create_sub_catg1.setEnabled(True)
            if self.btn_delete_item_catg1:
                self.btn_delete_item_catg1.setEnabled(False)
        elif isinstance(selected_object, CategoryLower):
            # Disable category creation when CategoryLower is selected
            if self.input_new_sub_catg1:
                self.input_new_sub_catg1.setEnabled(False)
            if self.btn_create_sub_catg1:
                self.btn_create_sub_catg1.setEnabled(False)
            if self.input_new_element_catg1:
                self.input_new_element_catg1.setEnabled(True)
            if self.btn_create_element_catg1:
                self.btn_create_element_catg1.setEnabled(True)
            if self.inputElementQtCatg1:
                self.inputElementQtCatg1.setEnabled(True)
            if self.btn_delete_item_catg1:
                self.btn_delete_item_catg1.setEnabled(True)
        if isinstance(selected_object, Element):
            # Disable element creation when Project is selected
            print ("Is instance")
            if self.input_new_element_catg1:
                self.input_new_element_catg1.setEnabled(False)
            if self.btn_create_element_catg1:
                self.btn_create_element_catg1.setEnabled(False)
            if self.inputElementQtCatg1:
                self.inputElementQtCatg1.setEnabled(False)
            if self.input_new_sub_catg1:
                self.input_new_sub_catg1.setEnabled(False)
            if self.btn_create_sub_catg1:
                self.btn_create_sub_catg1.setEnabled(False)
            if self.btn_delete_item_catg1:
                self.btn_delete_item_catg1.setEnabled(True)
        elif isinstance(selected_object, CategoryHigher):
            # Enable category creation for CategoryHigher
            if self.input_new_sub_catg1:
                self.input_new_sub_catg1.setEnabled(True)
            if self.btn_create_sub_catg1:
                self.btn_create_sub_catg1.setEnabled(True)
            if self.btn_delete_item_catg1:
                self.btn_delete_item_catg1.setEnabled(True)

            # Enable element creation for CategoryHigher only if it has no children
            if selected_object.children:
                if self.input_new_element_catg1:
                    self.input_new_element_catg1.setEnabled(False)
                if self.btn_create_element_catg1:
                    self.btn_create_element_catg1.setEnabled(False)
                if self.inputElementQtCatg1:
                    self.inputElementQtCatg1.setEnabled(False)
            else:
                if self.input_new_element_catg1:
                    self.input_new_element_catg1.setEnabled(True)
                if self.btn_create_element_catg1:
                    self.btn_create_element_catg1.setEnabled(True)
                if self.inputElementQtCatg1:
                    self.inputElementQtCatg1.setEnabled(True)

    def add_new_category(self):
        category_name = self.input_new_sub_catg1.text().strip()
        if not category_name:
            return

        selected_item = self.tree_widget.currentItem()
        parent_object = None

        if selected_item:
            parent_object = selected_item.data(0, Qt.UserRole)

        new_category = CategoryHigher(name=category_name)
        object_to_reselect = None # Initialize object to reselect

        if parent_object is None: # No item selected, add to the current project
            self.app_window.current_project.add_category(new_category)
            object_to_reselect = self.app_window.current_project
        elif isinstance(parent_object, Project): # Project is selected
            parent_object.add_category(new_category)
            object_to_reselect = parent_object
        elif isinstance(parent_object, CategoryHigher): # CategoryHigher is selected
            parent_object.add_child(new_category)
            object_to_reselect = parent_object
        # If parent_object is CategoryLower, the UI should have disabled the button, so no action needed here.

        self.populate_project_tree()
        self.input_new_sub_catg1.clear()
        self.app_window.project_modified = True

        # Re-select the parent object in the tree to maintain context
        if object_to_reselect:
            item = self.find_tree_item_for_object(object_to_reselect, self.tree_widget.invisibleRootItem())
            if item:
                self.tree_widget.setCurrentItem(item)
                self.tree_widget.expandItem(item)
        print(new_category.to_dict())

    def _replace_category_in_model(self, project_or_category, old_category_id, new_category):
        if isinstance(project_or_category, Project):
            for i, category in enumerate(project_or_category.categories):
                if category.id == old_category_id:
                    project_or_category.categories[i] = new_category
                    return True
                if self._replace_category_in_model(category, old_category_id, new_category):
                    return True
        elif isinstance(project_or_category, CategoryHigher):
            for i, category in enumerate(project_or_category.children):
                if category.id == old_category_id:
                    project_or_category.children[i] = new_category
                    return True
                if self._replace_category_in_model(category, old_category_id, new_category):
                    return True
        return False

    def handle_export_all_bars(self):
        if self.app_window.current_project:
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Export Project Data to Excel", "project_data.xlsx", "Excel Files (*.xlsx)"
            )
            if file_name:
                ExcelExporter.export_project_bars_to_excel(self.app_window.current_project, file_name)
        else:
            QMessageBox.warning(self, "Export Error", "No project loaded to export.")

    def add_new_element(self):
        element_name = self.input_new_element_catg1.text().strip()
        if not element_name:
            print(element_name)
            QMessageBox.warning(self, "Input Error", "Please enter a valid element name.")
            return

        quantity_text = self.inputElementQtCatg1.text().strip()
        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number.")
        except ValueError as e:
            QMessageBox.warning(self, "Input Error", f"Invalid quantity: {e}. Please enter a valid positive number.")
            return

        selected_items = self.tree_widget.selectedItems()
        if not selected_items:
            # No item selected, cannot add element
            return

        selected_object = selected_items[0].data(0, Qt.UserRole)
        parent_object = selected_object # In this context, the selected object is the parent for the new element

        if parent_object is None or isinstance(parent_object, Project):
            # Cannot add element directly to Project or if no object is selected
            print("Please select a Category (Higher or Lower) to add an element.")
            return

        object_to_reselect = None
        new_element = None

        if isinstance(parent_object, CategoryLower):
            new_element = Element(name=element_name, quantity=quantity)
            parent_object.add_element(new_element)
            object_to_reselect = parent_object
        elif isinstance(parent_object, CategoryHigher):
            if parent_object.children:
                print("Cannot add elements to a CategoryHigher that already contains sub-categories.")
                return
            
            # Convert CategoryHigher to CategoryLower
            new_category_lower = CategoryLower(name=parent_object.name)
            new_category_lower.id = parent_object.id
            new_category_lower.parent_tree = parent_object.parent_tree
            new_element = Element(name=element_name, quantity=quantity)
            new_category_lower.add_element(new_element)

            # Replace the old CategoryHigher with the new CategoryLower in the project structure
            self._replace_category_in_model(self.app_window.current_project, parent_object.id, new_category_lower)
            object_to_reselect = new_category_lower
            print("New Category created: ", new_category_lower.to_dict())

        self.populate_project_tree()
        self.input_new_element_catg1.clear()
        self.inputElementQtCatg1.clear()
        self.app_window.project_modified = True

        if object_to_reselect:
            item = self.find_tree_item_for_object(object_to_reselect, self.tree_widget.invisibleRootItem())
            if item:
                self.tree_widget.setCurrentItem(item)
                self.tree_widget.expandItem(item)
        print("New Element: ", new_element.to_dict())
    def populate_project_tree(self):
        #Recursive function to populate tree widget
        print("Populating project tree...")
        def _add_items(parent_item, obj_list):
            for obj in obj_list:
                tree_item = QTreeWidgetItem(parent_item, [obj.name])
                tree_item.setData(0, Qt.UserRole, obj)  # Store the actual object
                if hasattr(obj, 'children') and obj.children:
                    print("Inside")
                    _add_items(tree_item, obj.children)
                if hasattr(obj, 'elements') and obj.elements:
                    _add_items(tree_item, obj.elements)
        self.tree_widget.clear()

        project_item = QTreeWidgetItem(self.tree_widget, [self.app_window.current_project.name])
        project_item.setData(0, Qt.UserRole, self.app_window.current_project)  # Store the actual project object
        _add_items(project_item, self.app_window.current_project.categories)
        self.tree_widget.expandAll()


    def find_tree_item_for_object(self, obj, start_item=None):
        """Recursively finds the QTreeWidgetItem associated with a given data object."""
        if start_item is None:
            start_item = self.tree_widget.invisibleRootItem()

        for i in range(start_item.childCount()):
            child_item = start_item.child(i)
            item_object = child_item.data(0, Qt.UserRole)
            if item_object is obj: # Direct object comparison
                return child_item
            
            # Recursively search in children
            found_item = self.find_tree_item_for_object(obj, child_item)
            if found_item:
                return found_item
        return None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.tree_widget:
            header = self.tree_widget.header()
            total_width = self.tree_widget.viewport().width()
            header.resizeSection(0, int(total_width * 0.66))  # ~2/3
            header.resizeSection(1, int(total_width * 0.34))  # ~1/3

    def prompt_save_project(self):
        if not self.app_window.project_modified:
            self.app_window.go_to_main_menu_screen()
            return

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Project")
        msg_box.setText("Do you want to save changes to your project?")
        msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Save) # Make 'Save' the default action

        ret = msg_box.exec() # Execute the message box and get the user's choice

        if ret == QMessageBox.Save:
            self.save_project_and_go_back() # Call method to save and then navigate
        elif ret == QMessageBox.Discard:
            self.app_window.go_to_main_menu_screen() # Navigate without saving
        # If ret == QMessageBox.Cancel, we do nothing, and the screen will not change.

    def save_current_project(self):
        if not self.app_window.project_modified:
            QMessageBox.information(self, "No Changes", "No changes have been made since the last save.")
            return True # Indicate that no saving was needed, but operation was successful

        if self.app_window.current_project:
            file_name = self.app_window.current_project_file_path

            if not file_name:
                options = QFileDialog.Options()
                default_filename = self.app_window.current_project.name + ".gbbs"
                file_name, _ = QFileDialog.getSaveFileName(self, "Save Project",
                                                           default_filename,
                                                           "GenBBS Project Files (*.gbbs);;All Files (*)",
                                                           options=options)

            if file_name:
                if not file_name.endswith(".gbbs"):
                    file_name += ".gbbs"
                try:
                    project_data = self.app_window.current_project.to_dict()
                    with open(file_name, 'w') as f:
                        json.dump(project_data, f, indent=4)
                    QMessageBox.information(self, "GenBBS", "Save Successful")
                    self.app_window.project_modified = False
                    self.app_window.current_project_file_path = file_name
                    return True # Indicate successful save
                except Exception as e:
                    QMessageBox.critical(self, "Save Error", f"Could not save project: {e}")
                    return False # Indicate failed save
            else:
                return False # User cancelled save dialog
        else:
            QMessageBox.warning(self, "No Project", "No active project to save.")
            return False # No project to save

    def save_project_and_go_back(self):
        if self.save_current_project(): # Call the new save method
            self.app_window.go_to_main_menu_screen()

    def _on_edit_name_button_clicked(self):
        selected_items = self.tree_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Edit Name", "Please select an item to edit its name.")
            return

        selected_tree_item = selected_items[0]
        selected_object = selected_tree_item.data(0, Qt.UserRole)

        # if selected_object == self.app_window.current_project:
        #     QMessageBox.warning(self, "Edit Name", "Cannot edit the name of the root project.")
        #     return

        current_name = selected_object.name
        new_name, ok = QInputDialog.getText(self, "Edit Name", "Enter new name:", QLineEdit.Normal, current_name)

        if ok and new_name and new_name != current_name:
            selected_object.name = new_name
            self.app_window.project_modified = True
            self.populate_project_tree()
            self.update_selected_item() # Refresh the display of the selected item
            # Re-select the item after repopulating the tree
            item = self.find_tree_item_for_object(selected_object, self.tree_widget.invisibleRootItem())
            if item:
                self.tree_widget.setCurrentItem(item)
                self.tree_widget.expandItem(item)
        elif ok and not new_name:
            QMessageBox.warning(self, "Edit Name", "Name cannot be empty.")


class ElementManagementScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_element.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

class ReinforcementScreen(QWidget):
    def __init__(self, parent=None, settings_manager=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        self.settings_manager = settings_manager
        self.loaded_ui = QUiLoader().load("assets/ui/GenBBS_reinf.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(self.loaded_ui)
        self.setLayout(layout)
        self.element = None

        # Connect the back button
       
        # Initialize QLabel for element hierarchy
        self.lbl_element_hierarchy = self.loaded_ui.findChild(QLabel, "labelHeaderReinf")
        self.connect_ui_elements()
        self.populate_combo_boxes()
        self.update_shape_image()
        self._update_dimension_input_states()
        self._apply_settings() # Apply settings on initialization

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.settings_manager.get_setting("reinforcement/chBoxAllowKeySett") == "true":
                self.btn_next_reinf.click()
                event.accept()
            else:
                super().keyPressEvent(event)
        else:
            super().keyPressEvent(event)

    def connect_ui_elements(self):
        # Line Edits
        self.btn_back_reinf = self.loaded_ui.findChild(QPushButton, "btnBackReinf")
        self.btn_back_reinf.clicked.connect(self.go_back_to_category1_screen)
        self.btn_save_reinf = self.loaded_ui.findChild(QPushButton, "btnSaveReinf")
        self.btn_save_reinf.clicked.connect(self.save_current_project)
        self.input_bar_size_reinf = self.loaded_ui.findChild(QComboBox, "inputBarSizeReinf")
        self.shape_code_reinf = self.loaded_ui.findChild(QComboBox, "inputShapeCodeReinf")
        self.input_bar_mark = self.loaded_ui.findChild(QLineEdit, "inputBarMark")
        self.input_no_of_bars = self.loaded_ui.findChild(QLineEdit, "inputNoOfBars")
        self.a_dimension = self.loaded_ui.findChild(QLineEdit, "aDimension")
        self.e_dimension = self.loaded_ui.findChild(QLineEdit, "eDimension")
        self.b_dimension = self.loaded_ui.findChild(QLineEdit, "bDimension")
        self.c_dimension = self.loaded_ui.findChild(QLineEdit, "cDimension")
        self.f_dimension = self.loaded_ui.findChild(QLineEdit, "fDimension")
        self.r_dimension = self.loaded_ui.findChild(QLineEdit, "rDimension")
        self.d_dimension = self.loaded_ui.findChild(QLineEdit, "dDimension")
        # Buttons
        self.btn_serial_no_reinf = self.loaded_ui.findChild(QPushButton, "serialNoReinf")
        self.btn_next_reinf = self.loaded_ui.findChild(QPushButton, "btnNextReinf")
        self.btn_next_reinf.clicked.connect(self.create_bar_from_inputs)
        self.btn_back_reinf = self.loaded_ui.findChild(QPushButton, "btnBackReinf")

        # Labels
        self.label_header_reinf = self.loaded_ui.findChild(QLabel, "labelHeaderReinf")
        self.element_no_reinf = self.loaded_ui.findChild(QLineEdit, "elementNoReinf") # Changed from QLabel to QLineEdit
        self.label_formula_reinf = self.loaded_ui.findChild(QLabel, "formulaReinf")
        self.label_shape_display_reinf = self.loaded_ui.findChild(QLabel, "shapeDisplayReinf")
        self.label_quantity_reinf = self.loaded_ui.findChild(QLabel, "labelQtReinf")
        self.shape_code_reinf.currentIndexChanged.connect(self.update_shape_image)
        self.shape_code_reinf.currentIndexChanged.connect(self._update_dimension_input_states)
        self.element_no_reinf.editingFinished.connect(self._update_element_quantity)


        # Table Widget
        self.table_widget_reinf = self.loaded_ui.findChild(QTableWidget, "tableWidgetReinf")
        # self.table_widget_reinf.itemChanged.connect(self.handle_bar_table_item_changed)
        self.table_widget_reinf.itemSelectionChanged.connect(self.load_bar_data_to_form)
        self.btn_delete_item_catg1 = self.loaded_ui.findChild(QPushButton, "btnDeleteItemCatg1")
        self.btn_delete_item_catg1.clicked.connect(self.delete_selected_bar)
        # self.table_widget_reinf.itemChanged.connect(self.handle_bar_table_item_changed)
        

        # Settings Button
        self.btn_settings_reinf = self.loaded_ui.findChild(QPushButton, "btnSettingsReinf")
        if self.btn_settings_reinf:
            self.btn_settings_reinf.clicked.connect(self._open_settings_dialog)

    def _open_settings_dialog(self):
        settings_dialog = SettingsScreen(self.settings_manager, self)
        print("Settings before opening dialog: \n")
        for key in self.settings_manager.settings.allKeys():
            value = self.settings_manager.settings.value(key)
            print(f"{key}: {value}")
        print("\n")
        settings_dialog._populate_ui_from_settings()
        if settings_dialog.exec() == QDialog.Accepted:
            # Settings were saved, re-apply them to the ReinforcementScreen
            self._apply_settings()

    def _apply_settings(self):
        # Retrieve settings
        map_bool = {"true": True, "false": False}
        is_autofill_enabled= map_bool[self.settings_manager.get_setting("reinforcement/chBoxAutoFillSett")]
        is_autogen_enabled = map_bool[self.settings_manager.get_setting("reinforcement/chBoxAutoGenSett")]   
        is_allowkey_enabled = map_bool[self.settings_manager.get_setting("reinforcement/chBoxAllowKeySett")]  

        no_of_bars = self.settings_manager.get_setting("reinforcement/noOfBarsSett")
        if is_autofill_enabled == True: 
            print("\n\n\n\n Autofill is enabledd!!!  \n\n")
            a_dim = self.settings_manager.get_setting("reinforcement/aSett")
            b_dim = self.settings_manager.get_setting("reinforcement/bSett")
            c_dim = self.settings_manager.get_setting("reinforcement/cSett")
            d_dim = self.settings_manager.get_setting("reinforcement/dSett")
            e_dim = self.settings_manager.get_setting("reinforcement/eSett")
            f_dim = self.settings_manager.get_setting("reinforcement/fSett")
            r_dim = self.settings_manager.get_setting("reinforcement/rSett")
            bar_size = self.settings_manager.get_setting("reinforcement/barSizeSett")
            shape_code = self.settings_manager.get_setting("reinforcement/shapeCodeSett")
        

            # Apply settings to UI elements
            self.input_no_of_bars.setText(str(no_of_bars))
            self.a_dimension.setText(str(a_dim))
            self.b_dimension.setText(str(b_dim))
            self.c_dimension.setText(str(c_dim))
            self.d_dimension.setText(str(d_dim))
            self.e_dimension.setText(str(e_dim))
            self.f_dimension.setText(str(f_dim))
            self.r_dimension.setText(str(r_dim))

            # Set current text for combo boxes, ensuring the value exists in the combo box
            index = self.input_bar_size_reinf.findText(bar_size)
            if bar_size == "":
                self.input_bar_size_reinf.setCurrentText("")
            if index != -1:
                self.input_bar_size_reinf.setCurrentIndex(index)
            
            index = self.shape_code_reinf.findText(str(shape_code))
            if shape_code == "":
                self.shape_code_reinf.setCurrentText("")
            if index != -1:
                self.shape_code_reinf.setCurrentIndex(index)

        print(f"Auto-fill setting applied: {is_autofill_enabled}")
        print(f"Auto-generate setting applied: {is_autogen_enabled}")
        print(f"Allow key setting applied: {is_allowkey_enabled}")

    def _generate_next_bar_mark(self):
        if not self.element or not self.element.bars:
            return 1
        
        existing_marks = [bar.bar_mark for bar in self.element.bars if isinstance(bar.bar_mark, int) or (isinstance(bar.bar_mark, str) and bar.bar_mark.isdigit())]
        if not existing_marks:
            return 1
        
        return max(int(mark) for mark in existing_marks) + 1

    def delete_selected_bar(self):
        selected_rows = self.table_widget_reinf.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.information(self, "No Selection", "Please select one or more bars to delete.")
            return

        reply = QMessageBox.question(self, 'Delete Bars',
                                     f"Are you sure you want to delete {len(selected_rows)} selected bar(s)?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Sort in reverse order to delete from the end, avoiding index issues
            rows_to_delete = sorted([index.row() for index in selected_rows], reverse=True)
            
            for row_index in rows_to_delete:
                if 0 <= row_index < len(self.element.bars):
                    del self.element.bars[row_index]
            
            self.populate_bars_table() # Refresh the table display once after all deletions
            QMessageBox.information(self, "Deletion Successful", f"{len(selected_rows)} selected bar(s) have been deleted.")
            self.app_window.project_modified = True
        
        self.table_widget_reinf.resizeColumnsToContents()

    def handle_bar_table_item_changed(self, item):
        # Disconnect to prevent recursive calls during programmatic updates
        self.table_widget_reinf.itemChanged.disconnect(self.handle_bar_table_item_changed)

        row = item.row()
        col = item.column()
        new_value = item.text()

        if not self.element or row >= len(self.element.bars):
            # Reconnect and return if no element or invalid row
            self.table_widget_reinf.itemChanged.connect(self.handle_bar_table_item_changed)
            return

        bar = self.element.bars[row]
        updated = False

        try:
            if col == 0:  # Bar Mark
                bar.bar_mark = new_value
                updated = True
            elif col == 1:  # Shape Code
                if new_value in SHAPE_CODE_LENGTH_MAP:
                    bar.shape_code = new_value
                    updated = True
                else:
                    QMessageBox.warning(self, "Invalid Input", f"Invalid Shape Code: {new_value}. Please enter a valid shape code.")
                    item.setText(bar.shape_code) # Revert to original value
            elif col == 2:  # Diameter
                # Assuming diameter is stored as a string like "Y10", extract the number
                diameter_str = new_value.lstrip('Yy')
                if diameter_str.isdigit() and int(diameter_str) in MIN_BEND_RADII:
                    bar.diameter = new_value # Store as "YXX"
                    updated = True
                else:
                    QMessageBox.warning(self, "Invalid Input", f"Invalid Diameter: {new_value}. Please enter a valid diameter (e.g., 'Y10').")
                    item.setText(bar.diameter) # Revert to original value
            elif col == 4:  # Number of Bars
                if new_value.isdigit() and int(new_value) > 0:
                    bar.number_of_bars = int(new_value)
                    updated = True
                else:
                    QMessageBox.warning(self, "Invalid Input", "Number of Bars must be a positive integer.")
                    item.setText(str(bar.number_of_bars)) # Revert to original value

            if updated:
                # Recalculate cut length and weights if relevant properties changed
                # This assumes that changing bar_mark, shape_code, diameter, or number_of_bars
                # might affect cut_length, unit_weight, or total_weight.
                # You might need to call a specific recalculation method here.
                # For now, we'll just mark project as modified and repopulate.
                bar.recalculate_properties()  # Trigger recalculation
                self.app_window.project_modified = True
                # Re-populate the table to reflect any calculated changes (e.g., cut length, weights)
                self.populate_bars_table()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while updating bar data: {e}")
            # Revert the item text to its original value if an error occurs
            self.populate_bars_table() # A full refresh is safer here

        # Reconnect the signal
        self.table_widget_reinf.itemChanged.connect(self.handle_bar_table_item_changed)
    def clear_input_fields(self):
        self.input_bar_mark.clear()
        map_bool = {"true": True, "false": False}
        is_autogen_enabled = map_bool[self.settings_manager.get_setting("reinforcement/chBoxAutoGenSett")]
        if is_autogen_enabled:
            self.input_bar_mark.setText(str(self._generate_next_bar_mark()))
        self.input_no_of_bars.clear()
        self.input_bar_size_reinf.setCurrentIndex(0)  # Reset combo box to first item
        self.shape_code_reinf.setCurrentIndex(0)  # Reset combo box to first item
        self.a_dimension.clear()
        self.e_dimension.clear()
        self.b_dimension.clear()
        self.c_dimension.clear()
        self.f_dimension.clear()
        self.r_dimension.clear()
        self.d_dimension.clear()
        self._apply_settings()

    def load_bar_data_to_form(self):
        selected_rows = self.table_widget_reinf.selectionModel().selectedRows()
        if selected_rows:
            row = selected_rows[0].row()
            if 0 <= row < len(self.element.bars):
                bar = self.element.bars[row]
                self.input_bar_mark.setText(str(bar.bar_mark))
                self.input_no_of_bars.setText(str(bar.number_of_bars))

                # Set diameter combo box
                diameter_index = self.input_bar_size_reinf.findText(bar.diameter)
                if diameter_index != -1:
                    self.input_bar_size_reinf.setCurrentIndex(diameter_index)

                # Set shape code combo box
                shape_code_index = self.shape_code_reinf.findText(bar.shape_code)
                if shape_code_index != -1:
                    self.shape_code_reinf.setCurrentIndex(shape_code_index)

                # Set dimensions
                self.a_dimension.setText(str(bar.lengths.get("A", "")))
                self.e_dimension.setText(str(bar.lengths.get("E", "")))
                self.b_dimension.setText(str(bar.lengths.get("B", "")))
                self.c_dimension.setText(str(bar.lengths.get("C", "")))
                self.f_dimension.setText(str(bar.lengths.get("F", "")))
                self.r_dimension.setText(str(bar.lengths.get("R", "")))
                self.d_dimension.setText(str(bar.lengths.get("D", "")))
            else:
                self.clear_input_fields()
        else:
            self.clear_input_fields()

    def populate_combo_boxes(self):
        # Clear existing items before populating
        self.input_bar_size_reinf.clear()
        # Extract unique bar sizes from MIN_BEND_RADII keys and sort them
        bar_sizes = sorted(list(MIN_BEND_RADII.keys()))
        for size in bar_sizes:
            self.input_bar_size_reinf.addItem(f"Y{size}")

        # Populate Shape Code ComboBox
        self.shape_code_reinf.clear()
        # Extract shape codes from SHAPE_CODE_LENGTH_MAP keys and sort them
        shape_codes = sorted(list(SHAPE_CODE_LENGTH_MAP.keys()))
        
        image_base_path = "assets/images/"
        for code in shape_codes:
            image_path = f"{image_base_path}{code}.jpg"
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon = QIcon(scaled_pixmap)
                self.shape_code_reinf.addItem(icon, code)
            else:
                self.shape_code_reinf.addItem(code) # Fallback if image not found
        
    def update_shape_image(self):
        self.update_formula_display()
        selected_shape_code = self.shape_code_reinf.currentText()
        print(selected_shape_code)
        if selected_shape_code:
            image_path = f":/images/{selected_shape_code}.jpg"
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                # Scale the pixmap to fit the label while maintaining aspect ratio
                scaled_pixmap = pixmap.scaled(self.label_shape_display_reinf.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.label_shape_display_reinf.setPixmap(pixmap)
            else:
                # Clear the label if image not found
                self.label_shape_display_reinf.clear()
        else:
            self.label_shape_display_reinf.clear()

    def _update_dimension_input_states(self):
        selected_shape_code = self.shape_code_reinf.currentText()
        required_dimensions = SHAPE_CODE_LENGTH_MAP.get(selected_shape_code, [])

        # List of all dimension input fields
        dimension_inputs = {
            "A": self.a_dimension,
            "B": self.b_dimension,
            "C": self.c_dimension,
            "D": self.d_dimension,
            "E": self.e_dimension,
            "F": self.f_dimension,
            "R": self.r_dimension,
        }

        for dim_code, input_field in dimension_inputs.items():
            if dim_code in required_dimensions:
                input_field.setEnabled(True)
            else:
                # input_field.clear() # Clear the field if it's disabled
                input_field.setEnabled(False)

    def update_formula_display(self):
        selected_shape_code = self.shape_code_reinf.currentText()
        formula = SHAPE_CODE_FORMULA_STRINGS.get(selected_shape_code, "Formula not available")
        self.label_formula_reinf.setText(f"Formula: {formula}")

    def create_bar_from_inputs(self):
        print("Create Bar button clicked!")
        # Retrieve values from UI elements

        bar_size_text = self.input_bar_size_reinf.currentText()
        shape_code = self.shape_code_reinf.currentText()
        bar_mark_text = self.input_bar_mark.text()
        no_of_bars_text = self.input_no_of_bars.text()
        print(f"Bar Size: {bar_size_text}, Shape Code: {shape_code}, Bar Mark: {bar_mark_text}, No of Bars: {no_of_bars_text}")

        dimensions = {
            "A": self.a_dimension.text(),
            "E": self.e_dimension.text(),
            "B": self.b_dimension.text(),
            "C": self.c_dimension.text(),
            "F": self.f_dimension.text(),
            "R": self.r_dimension.text(),
            "D": self.d_dimension.text(),
        }
        print(dimensions)
        
        # Basic validation and conversion
        try:
            if int(''.join(filter(str.isdigit, bar_size_text))) not in MIN_BEND_RADII.keys():
                QMessageBox.warning(self, "Input Error", "Please select a valid Bar Size.")
                return
            if shape_code not in SHAPE_CODE_LENGTH_MAP.keys():
                QMessageBox.warning(self, "Input Error", "Please select a valid Shape Code.")
                return
            bar_mark = int(bar_mark_text)
            number_of_bars = int(no_of_bars_text)
            # Convert dimensions to float, only if they are not empty
            lengths = {}
            for key, value in dimensions.items():
                if key in SHAPE_CODE_LENGTH_MAP[shape_code] and (float(value) == 0 or value == ""):
                    QMessageBox.warning(self, "Input Error", "Please enter valid numbers for dimensions.")
                    return
                if value:
                    lengths[key] = float(value)

        except Exception as e:
            print(f"{e}\n There was an error here \n")
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers for Bar Mark, Number of Bars, and dimensions.")
            return

        if not bar_size_text or not shape_code:
            QMessageBox.warning(self, "Input Error", "Please select both Bar Size and Shape Code.")
            return

        selected_rows = self.table_widget_reinf.selectionModel().selectedRows()
        if selected_rows: # Update existing bar
            row = selected_rows[0].row()
            if 0 <= row < len(self.element.bars):
                bar_to_update = self.element.bars[row]
                bar_to_update.bar_mark = bar_mark
                bar_to_update.shape_code = shape_code
                bar_to_update.diameter = bar_size_text
                bar_to_update.lengths = lengths
                bar_to_update.number_of_bars = number_of_bars
                bar_to_update.recalculate_properties() # Recalculate properties after update
                self.app_window.project_modified = True
                self.populate_bars_table()
                self.clear_input_fields()
                # self._apply_settings()
                self.table_widget_reinf.clearSelection() # Clear selection after update
                QMessageBox.information(self, "Bar Updated", f"Bar Mark {bar_mark} updated successfully.")
            else:
                QMessageBox.warning(self, "Update Error", "Selected row does not correspond to a valid bar.")
        else: # Create new bar
            # Create Bar object
            new_bar = Bar(
                bar_mark=bar_mark,
                shape_code=shape_code,
                diameter=bar_size_text, # Assuming bar_size is the diameter string (e.g., 'Y10')
                lengths=lengths,
                number_of_bars=number_of_bars,
                parent_tree=self.element.parent_tree + [{'id': self.element.id, 'name': self.element.name, 'type': 'Element'}]
            )

            # Add bar to the current element
            if self.element:
                self.element.add_bar(new_bar)
                self.app_window.project_modified = True
                self.populate_bars_table()
                self.clear_input_fields() # Clear input fields after successful bar creation
                # self._apply_settings()
                # QMessageBox.information(self, "Bar Created", f"New Bar Mark {bar_mark} created successfully.")
            else:
                QMessageBox.warning(self, "No Element Selected", "Please select an element before adding bars.")

        # Placeholder for UI update logic
        pass


    def populate_bars_table(self):
        self.table_widget_reinf.setRowCount(0) # Clear existing rows
        if not self.element or not self.element.bars:
            return

        # Set table headers
        headers = ["Bar Mark", "Shape Code", "Diameter", "Lengths", "Number of Bars", "Cut Length", "Unit Weight", "Total Weight"]
        self.table_widget_reinf.setColumnCount(len(headers))
        self.table_widget_reinf.setHorizontalHeaderLabels(headers)

        for row, bar in enumerate(self.element.bars):
            self.table_widget_reinf.insertRow(row)
            self.table_widget_reinf.setItem(row, 0, QTableWidgetItem(str(bar.bar_mark)))
            self.table_widget_reinf.setItem(row, 1, QTableWidgetItem(bar.shape_code))
            self.table_widget_reinf.setItem(row, 2, QTableWidgetItem(bar.diameter))
            self.table_widget_reinf.setItem(row, 3, QTableWidgetItem(str(bar.lengths)))
            self.table_widget_reinf.setItem(row, 4, QTableWidgetItem(str(bar.number_of_bars)))
            self.table_widget_reinf.setItem(row, 5, QTableWidgetItem(f"{bar.cut_length:.2f} mm"))
            self.table_widget_reinf.setItem(row, 6, QTableWidgetItem(f"{bar.unit_weight:.2f} kg/m"))
            self.table_widget_reinf.setItem(row, 7, QTableWidgetItem(f"{bar.total_weight:.2f} kg"))

        self.table_widget_reinf.resizeColumnsToContents()

    def set_element(self, element):
        self.element = element
        # Construct and display the parent hierarchy
        hierarchy_names = [item['name'] for item in element.parent_tree] + [element.name]
        self.lbl_element_hierarchy.setText(" > ".join(hierarchy_names))
        self.element_no_reinf.setText(f"{self.element.quantity}")
        self.label_quantity_reinf.setText(f"Quantity of {self.element.name}:")
        print(f"ReinforcementScreen received element: {self.element.name}")
        self.populate_bars_table() # Populate table when element is set

    def _update_element_quantity(self):
        if not self.element:
            return

        try:
            new_quantity = int(self.element_no_reinf.text())
            if new_quantity <= 0:
                QMessageBox.warning(self, "Invalid Input", "Quantity must be a positive integer.")
                self.element_no_reinf.setText(str(self.element.quantity)) # Revert to original
                return
            
            if self.element.quantity != new_quantity:
                self.element.quantity = new_quantity
                self.app_window.project_modified = True
                # QMessageBox.information(self, "Quantity Updated", f"Element quantity updated to {new_quantity}.")

        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for quantity.")
            self.element_no_reinf.setText(str(self.element.quantity)) # Revert to original
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            self.element_no_reinf.setText(str(self.element.quantity)) # Revert to original


    def go_back_to_category1_screen(self):
        # This method will be connected to a 'Back' button in the UI
        self.app_window.go_to_category1_screen()
        self.element = None

    def save_current_project(self):
        if not self.app_window.project_modified:
            QMessageBox.information(self, "No Changes", "No changes have been made since the last save.")
            return True # Indicate that no saving was needed, but operation was successful

        if self.app_window.current_project:
            file_name = self.app_window.current_project_file_path

            if not file_name:
                options = QFileDialog.Options()
                default_filename = self.app_window.current_project.name + ".gbbs"
                file_name, _ = QFileDialog.getSaveFileName(self, "Save Project",
                                                           default_filename,
                                                           "GenBBS Project Files (*.gbbs);;All Files (*)",
                                                           options=options)

            if file_name:
                if not file_name.endswith(".gbbs"):
                    file_name += ".gbbs"
                try:
                    project_data = self.app_window.current_project.to_dict()
                    with open(file_name, 'w') as f:
                        json.dump(project_data, f, indent=4)
                    QMessageBox.information(self, "GenBBS", "Save Successful")
                    self.app_window.project_modified = False
                    self.app_window.current_project_file_path = file_name
                    return True # Indicate successful save
                except Exception as e:
                    QMessageBox.critical(self, "Save Error", f"Could not save project: {e}")
                    return False # Indicate failed save
            else:
                return False # User cancelled save dialog
        else:
            QMessageBox.warning(self, "No Project", "No active project to save.")
            return False # No project to save

class SettingsScreen(QDialog):
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager
        self.loaded_ui = QUiLoader().load("assets/ui/settings.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(self.loaded_ui)
        # self._load_ui()
        self._connect_ui_elements()
        self._connect_signals()
        self._populate_combo_boxes()
        self._populate_ui_from_settings()

    def _connect_ui_elements(self):
        # Buttons
        self.btnSaveSett = self.loaded_ui.findChild(QPushButton, "btnSaveSett")
        self.btnCancelSett = self.loaded_ui.findChild(QPushButton, "btnCancelSett")
        # Checkboxes
        self.chBoxAutoFillSett = self.loaded_ui.findChild(QCheckBox, "chBoxAutoFillSett")
        self.chBoxAutoGenSett = self.loaded_ui.findChild(QCheckBox, "chBoxAutoGenSett")
        self.chBoxAllowKeySett = self.loaded_ui.findChild(QCheckBox, "chBoxAllowKeySett")
        # Line Edits
        self.noOfBarsSett = self.loaded_ui.findChild(QLineEdit, "noOfBarsSett")
        self.aSett = self.loaded_ui.findChild(QLineEdit, "aSett")
        self.bSett = self.loaded_ui.findChild(QLineEdit, "bSett")
        self.cSett = self.loaded_ui.findChild(QLineEdit, "cSett")
        self.dSett = self.loaded_ui.findChild(QLineEdit, "dSett")
        self.eSett = self.loaded_ui.findChild(QLineEdit, "eSett")
        self.fSett = self.loaded_ui.findChild(QLineEdit, "fSett")
        self.rSett = self.loaded_ui.findChild(QLineEdit, "rSett")
        # ComboBoxes
        self.barSizeSett = self.loaded_ui.findChild(QComboBox, "barSizeSett")
        self.shapeCodeSett = self.loaded_ui.findChild(QComboBox, "shapeCodeSett")

    def _connect_signals(self):
        # Connect buttons
        self.btnSaveSett.clicked.connect(self.save_settings)
        self.btnCancelSett.clicked.connect(self.reject) # QDialog.reject() closes the dialog
        # Connect checkboxes
        self.chBoxAutoFillSett.stateChanged.connect(self._update_autofill_states)

    def _populate_combo_boxes(self):
        self.barSizeSett.clear()
        # Extract unique bar sizes from MIN_BEND_RADII keys and sort them
        bar_sizes = sorted(list(MIN_BEND_RADII.keys()))
        self.barSizeSett.addItem("")
        for size in bar_sizes:
            self.barSizeSett.addItem(f"Y{size}")
        # Populate Shape Code ComboBox
        self.shapeCodeSett.clear()
        # Extract shape codes from SHAPE_CODE_LENGTH_MAP keys and sort them
        shape_codes = sorted(list(SHAPE_CODE_LENGTH_MAP.keys()))
        
        image_base_path = "assets/images/"
        self.shapeCodeSett.addItem("")
        for code in shape_codes:
            image_path = f"{image_base_path}{code}.jpg"
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon = QIcon(scaled_pixmap)
                self.shapeCodeSett.addItem(icon, code)
            else:
                self.shapeCodeSett.addItem(code) # Fallback if image not found
        

    def _populate_ui_from_settings(self):
        # Checkboxes
        print("Settings before opening dialog in dialog itself: \n")
        for key in self.settings_manager.settings.allKeys():
            value = self.settings_manager.settings.value(key)
            print(f"{key}: {value}")
        print("\n")
        map_bool = {"true": True, "false": False}
        self.chBoxAutoFillSett.setChecked(map_bool[self.settings_manager.get_setting("reinforcement/chBoxAutoFillSett")])
        self.chBoxAutoGenSett.setChecked(map_bool[self.settings_manager.get_setting("reinforcement/chBoxAutoGenSett")])    
        self.chBoxAllowKeySett.setChecked(map_bool[self.settings_manager.get_setting("reinforcement/chBoxAllowKeySett")])   

        self.noOfBarsSett.setText(str(self.settings_manager.get_setting("reinforcement/noOfBarsSett")))
        self.aSett.setText(str(self.settings_manager.get_setting("reinforcement/aSett")))
        self.bSett.setText(str(self.settings_manager.get_setting("reinforcement/bSett")))
        self.cSett.setText(str(self.settings_manager.get_setting("reinforcement/cSett")))
        self.dSett.setText(str(self.settings_manager.get_setting("reinforcement/dSett")))
        self.eSett.setText(str(self.settings_manager.get_setting("reinforcement/eSett")))
        self.fSett.setText(str(self.settings_manager.get_setting("reinforcement/fSett")))
        self.rSett.setText(str(self.settings_manager.get_setting("reinforcement/rSett")))
        # Assuming bar sizes are populated elsewhere or are static. For now, just set the current text.
        self.barSizeSett.setCurrentText(self.settings_manager.get_setting("reinforcement/barSizeSett"))
        # Assuming shape codes are populated elsewhere or are static. For now, just set the current text.
        self.shapeCodeSett.setCurrentText(str(self.settings_manager.get_setting("reinforcement/shapeCodeSett")))

    def save_settings(self):
        # Checkboxes
        print(f"Is autofill checked? {self.chBoxAutoFillSett.isChecked()}")
        self.settings_manager.set_setting("reinforcement/chBoxAutoFillSett", self.chBoxAutoFillSett.isChecked())
        print(self.settings_manager.get_setting("reinforcement/chBoxAutoFillSett"))
        self.settings_manager.set_setting("reinforcement/chBoxAutoGenSett", self.chBoxAutoGenSett.isChecked())
        self.settings_manager.set_setting("reinforcement/chBoxAllowKeySett", self.chBoxAllowKeySett.isChecked())
        def safe_int(text):
            if text.strip() == "":
                return None
            try:
                return int(text)
            except ValueError:
                raise ValueError("Invalid integer input")
        def safe_float(text):
            if text.strip() == "":
                print("ONE TEXT IS EMPTY")
                return None
            try:
                return float(text)
            except ValueError:
                raise ValueError("Invalid float input")
        if self.chBoxAutoFillSett.isChecked():
            try:
                a_val = safe_float(self.aSett.text())
                if a_val is not None:
                    self.settings_manager.set_setting("reinforcement/aSett", a_val)
                else:
                    self.settings_manager.set_setting("reinforcement/aSett", "")

                b_val = safe_float(self.bSett.text())
                if b_val is not None:
                    self.settings_manager.set_setting("reinforcement/bSett", b_val)
                else:
                    self.settings_manager.set_setting("reinforcement/bSett", "")

                c_val = safe_float(self.cSett.text())
                if c_val is not None:
                    self.settings_manager.set_setting("reinforcement/cSett", c_val)
                else:
                    self.settings_manager.set_setting("reinforcement/cSett", "")

                d_val = safe_float(self.dSett.text())
                if d_val is not None:
                    self.settings_manager.set_setting("reinforcement/dSett", d_val)
                else:
                    self.settings_manager.set_setting("reinforcement/dSett", "")

                e_val = safe_float(self.eSett.text())
                if e_val is not None:
                    self.settings_manager.set_setting("reinforcement/eSett", e_val)
                else:
                    self.settings_manager.set_setting("reinforcement/eSett", "")

                f_val = safe_float(self.fSett.text())
                if f_val is not None:
                    self.settings_manager.set_setting("reinforcement/fSett", f_val)
                else:
                    self.settings_manager.set_setting("reinforcement/fSett", "")

                r_val = safe_float(self.rSett.text())
                if r_val is not None:
                    self.settings_manager.set_setting("reinforcement/rSett", r_val)
                else:
                    self.settings_manager.set_setting("reinforcement/rSett", "")
                
                if self.barSizeSett.currentText() != "":
                    try:
                        if int(''.join(filter(str.isdigit, self.barSizeSett.currentText()))) not in MIN_BEND_RADII.keys():
                            QMessageBox.warning(self, "Input Error", "Please select a valid Bar Size.")
                            return
                    except ValueError:
                        QMessageBox.warning(self, "Input Error", "Please enter valid numbers for Bar Mark, Number of Bars, and dimensions.")
                        return
                if self.shapeCodeSett.currentText() not in SHAPE_CODE_LENGTH_MAP.keys() and self.shapeCodeSett.currentText() != "":
                    QMessageBox.warning(self, "Input Error", "Please select a valid Shape Code.")
                    return

                bar_size = self.barSizeSett.currentText()
                self.settings_manager.set_setting("reinforcement/barSizeSett", bar_size)

                shape_code_text = safe_int(self.shapeCodeSett.currentText())
                if shape_code_text is not None:
                    self.settings_manager.set_setting("reinforcement/shapeCodeSett", shape_code_text)
                else:
                    self.settings_manager.set_setting("reinforcement/shapeCodeSett", "")

                no_of_bars = safe_int(self.noOfBarsSett.text())
                if no_of_bars is not None:
                    self.settings_manager.set_setting("reinforcement/noOfBarsSett", no_of_bars)
                else:
                    self.settings_manager.set_setting("reinforcement/noOfBarsSett", "")
            except Exception as e:
                QMessageBox.warning(self, "Input Error", f"{e} Please enter valid numbers for all dimension and bar count fields.")
                return
        print("Before save: \n")
        for key in self.settings_manager.settings.allKeys():
            value = self.settings_manager.settings.value(key)
            print(f"{key}: {value}")
        print("\n")
        self.settings_manager.save_settings()
        print("After save: \n")
        for key in self.settings_manager.settings.allKeys():
            value = self.settings_manager.settings.value(key)
            print(f"{key}: {value}")
        print("\n")
        self.accept() # QDialog.accept() closes the dialog and returns QDialog.Accepted

    def _update_autofill_states(self):
        is_autofill_enabled = self.chBoxAutoFillSett.isChecked()
        # if not is_autofill_enabled:
        #     self.aSett.clear()
        #     self.bSett.clear()
        #     self.cSett.clear()
        #     self.dSett.clear()
        #     self.eSett.clear()
        #     self.fSett.clear()
        #     self.rSett.clear()
        #     self.noOfBarsSett.clear()
        #     self.barSizeSett.clear()
        #     self.shapeCodeSett.clear()

        # Dimension line edits
        self.aSett.setEnabled(is_autofill_enabled)
        self.bSett.setEnabled(is_autofill_enabled)
        self.cSett.setEnabled(is_autofill_enabled)
        self.dSett.setEnabled(is_autofill_enabled)
        self.eSett.setEnabled(is_autofill_enabled)
        self.fSett.setEnabled(is_autofill_enabled)
        self.rSett.setEnabled(is_autofill_enabled)

        # Number of bars line edit
        self.noOfBarsSett.setEnabled(is_autofill_enabled)
        # ComboBoxes
        self.barSizeSett.setEnabled(is_autofill_enabled)
        self.shapeCodeSett.setEnabled(is_autofill_enabled)

class SettingsManager:
    def __init__(self, organization="GenBBS", application="GenBBS"):
        self.settings = QSettings(organization, application)
        # self.settings.clear()
        self._default_settings = {
            "reinforcement/chBoxAutoFillSett": False,
            "reinforcement/chBoxAutoGenSett": False,
            "reinforcement/chBoxAllowKeySett": False,
            "reinforcement/aSett": "",
            "reinforcement/bSett": "",
            "reinforcement/cSett": "",
            "reinforcement/dSett": "",
            "reinforcement/eSett": "",
            "reinforcement/fSett": "",
            "reinforcement/rSett": "",
            "reinforcement/noOfBarsSett": "",
            "reinforcement/barSizeSett": "", # Default bar size
            "reinforcement/shapeCodeSett": "", # Default shape code
        }
        self._apply_default_settings_if_missing()

    def _apply_default_settings_if_missing(self):
        print("Inherreeeeee")
        for key, value in self._default_settings.items():
            if not self.settings.contains(key):
                self.settings.setValue(key, value)
        self.settings.sync() # Ensure defaults are written if not present

    def get_setting(self, key):
        return self.settings.value(key)

    def set_setting(self, key, value):
        self.settings.setValue(key, value)

    def save_settings(self):
        self.settings.sync()
        # Optional: force immediate write if needed for critical settings

# --- Main Application Window ---
class ApplicationWindow(QMainWindow):
    def __init__(self, splash_screen: QSplashScreen):
        super().__init__()
        self.splash_screen = splash_screen
        self.base_title = "GenBBS Application"
        self.setWindowTitle(self.base_title)
        self.setGeometry(100, 100, 800, 600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.current_project = None # Initialize current_project to None
        self.project_modified = False # Track if the current project has unsaved changes
        self.current_project_file_path = None # Track the file path of the current project
        self.settings_manager = SettingsManager()

        self.setup_screens()
        self.splash_screen.finish(self)

    def update_window_title(self, project_name: str = None):
        if project_name:
            self.setWindowTitle(f"{self.base_title} - {project_name}")
        else:
            self.setWindowTitle(self.base_title)

    def setup_screens(self):
        # Create screen instances
        self.loading_screen_widget = LoadingScreenWidget(self)
        self.main_menu_screen = MainMenuScreen(self)
        self.new_project_screen = NewProjectScreen(self)
        self.category1_screen = Category1Screen(self)
        self.reinforcement_screen = ReinforcementScreen(self, self.settings_manager)

        # Add screens to stacked widget
        self.stacked_widget.addWidget(self.loading_screen_widget)
        self.stacked_widget.addWidget(self.main_menu_screen)
        self.stacked_widget.addWidget(self.new_project_screen)
        self.stacked_widget.addWidget(self.category1_screen)
        self.stacked_widget.addWidget(self.reinforcement_screen)

        # Set initial screen
        self.go_to_main_menu_screen()

    def closeEvent(self, event):
        if self.project_modified:
            reply = QMessageBox.question(self, 'Save Changes?',
                                         "You have unsaved changes. Do you want to save them before exiting?",
                                         QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if reply == QMessageBox.Save:
                # Call save_current_project from Category1Screen
                if self.category1_screen.save_current_project():
                    event.accept() # Accept the close event if save is successful
                else:
                    event.ignore() # Ignore if save is cancelled or fails
            elif reply == QMessageBox.Discard:
                event.accept() # Accept the close event, discarding changes
            else:
                event.ignore() # Ignore the close event, user cancelled
        else:
            event.accept() # No unsaved changes, accept the close event

    def go_to_loading_screen(self):
        self.stacked_widget.setCurrentWidget(self.loading_screen_widget)

    def go_to_main_menu_screen(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_screen)
        self.update_window_title() # Clear project name from title
        self.stacked_widget.setCurrentIndex(1)

    def go_to_new_project_screen(self):
        self.stacked_widget.setCurrentIndex(2)

    def go_to_category1_screen(self):
        self.stacked_widget.setCurrentIndex(3) 
        print("Landed")
        self.category1_screen.setup_for_view()

    def show_reinforcement_screen(self, element):
        self.reinforcement_screen.set_element(element)
        self.reinforcement_screen.clear_input_fields()
        self.stacked_widget.setCurrentWidget(self.reinforcement_screen)


# --- Application Entry Point ---
if __name__ == "__main__":
    app = QApplication([])

    # Create a QPixmap from GenBBS_loading.ui for the QSplashScreen
    temp_loader = QUiLoader()
    temp_loading_widget = temp_loader.load("assets/ui/GenBBS_loading.ui")
    if temp_loading_widget:
        temp_loading_widget.setAttribute(Qt.WA_DontShowOnScreen)
        temp_loading_widget.resize(800, 600)
        pixmap = QPixmap(temp_loading_widget.size())
        temp_loading_widget.render(pixmap)
        del temp_loading_widget
    else:
        # Fallback if UI loading fails, use a default image or blank pixmap
        pixmap = QPixmap(400, 300)
        pixmap.fill(Qt.white)

    # Initialize and Show QSplashScreen
    splash_screen = QSplashScreen(pixmap)
    splash_screen.show()
    app.processEvents()

    # Simulate application initialization tasks
    splash_screen.showMessage("Initializing application...", Qt.AlignBottom | Qt.AlignCenter, Qt.black)
    app.processEvents()

    # Create and show the main application window
    main_application_window = ApplicationWindow(splash_screen)
    main_application_window.show()

    app.exec()

    

    

    