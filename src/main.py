from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplashScreen, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QFileDialog, QTreeWidget, QTreeWidgetItem, QHeaderView, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter # Re-adding QPixmap and QPainter
import resources
from src.logic.data_models import Project, CategoryHigher, CategoryLower, Element
import json
import os

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

        self.back_button.clicked.connect(self.prompt_save_project)
        self.save_button.clicked.connect(self.save_current_project)
        self.btn_create_sub_catg1.clicked.connect(self.add_new_category)      
        print("Connecting signal")  
        self.btn_create_element_catg1.clicked.connect(self.add_new_element)
        self.btn_delete_item_catg1.clicked.connect(self.delete_selected_item)

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
        self.input_new_element_catg1.setEnabled(False)
        self.btn_create_element_catg1.setEnabled(False)
        self.input_new_sub_catg1.setEnabled(False)
        self.btn_create_sub_catg1.setEnabled(False)
        self.btn_delete_item_catg1.setEnabled(False)
        

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
            self.app_window.show_reinforcement_screen(selected_object)
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

    def add_new_element(self):
        print("Here again")
        print(self.input_new_element_catg1.text())
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
            self.app_window.go_to_main_menu_screen() # Navigate after successful save
        # If save_current_project returns False, it means save was cancelled or failed, so stay on current screen


class ElementManagementScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_element.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

class ReinforcementScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_reinf.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)
        self.element = None

        # Connect the back button
        self.btn_back_reinf = loaded_ui.findChild(QPushButton, "btnBackReinf")
        self.btn_back_reinf.clicked.connect(self.go_back_to_category1_screen)

        # Initialize QLabel for element hierarchy
        self.lbl_element_hierarchy = loaded_ui.findChild(QLabel, "labelHeaderReinf")

    def set_element(self, element):
        self.element = element
        # Construct and display the parent hierarchy
        hierarchy_names = [item['name'] for item in element.parent_tree] + [element.name]
        self.lbl_element_hierarchy.setText(" > ".join(hierarchy_names))
        print(f"ReinforcementScreen received element: {self.element.name}")

    def go_back_to_category1_screen(self):
        # This method will be connected to a 'Back' button in the UI
        self.app_window.go_to_category1_screen()
        self.element = None


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
        self.reinforcement_screen = ReinforcementScreen(self)

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

    