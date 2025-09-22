from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplashScreen, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter # Re-adding QPixmap and QPainter
import resources
from src.logic.data_models import Project
import json # New import for JSON serialization
import os   # New import for path manipulation

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
            print(f"Selected file: {selected_file}")
            # TODO: Implement logic to load the selected project file

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
            project_name = project_name_input.text()
            if project_name:
                new_project = Project(name=project_name)
                self.app_window.current_project = new_project
                self.app_window.go_to_category1_screen()
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
        self.connect_buttons()

    def connect_buttons(self):
        back_button = self.loaded_ui.findChild(QPushButton, "btnBackCatg1")
        if back_button:
            back_button.clicked.connect(self.prompt_save_project) # Connect to new method

    def prompt_save_project(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Project")
        msg_box.setText("Do you want to save changes to your project?")
        msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Save) # Make 'Save' the default action

        ret = msg_box.exec() # Execute the message box and get the user's choice

        if ret == QMessageBox.Save:
            self.save_project_and_go_back() # Call method to save and then navigate
        elif ret == QMessageBox.Discard:
            self.app_window.go_to_new_project_screen() # Navigate without saving
        # If ret == QMessageBox.Cancel, we do nothing, and the screen will not change.

    def save_project_and_go_back(self):
        if self.app_window.current_project:
            options = QFileDialog.Options()
            # Suggest a default filename based on the project name
            default_filename = self.app_window.current_project.name + ".gbbs"
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Project",
                                                       default_filename,
                                                       "GenBBS Project Files (*.gbbs);;All Files (*)",
                                                       options=options)
            if file_name:
                # Ensure the file has the .gbbs extension
                if not file_name.endswith(".gbbs"):
                    file_name += ".gbbs"
                try:
                    project_data = self.app_window.current_project.to_dict()
                    with open(file_name, 'w') as f:
                        json.dump(project_data, f, indent=4)
                    QMessageBox.information(self, "Save Successful", f"Project saved to {os.path.basename(file_name)}")
                    self.app_window.go_to_new_project_screen() # Navigate after successful save
                except Exception as e:
                    QMessageBox.critical(self, "Save Error", f"Could not save project: {e}")
            else:
                # User cancelled the file dialog, stay on current screen
                pass
        else:
            QMessageBox.warning(self, "No Project", "No active project to save.")
            self.app_window.go_to_new_project_screen() # If no project, just go back

class Category2Screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app_window = parent # Store reference to ApplicationWindow
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_catg2.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

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

# --- Main Application Window ---
class ApplicationWindow(QMainWindow):
    def __init__(self, splash_screen: QSplashScreen):
        super().__init__()
        self.splash_screen = splash_screen
        self.setWindowTitle("GenBBS Application")
        self.setGeometry(100, 100, 800, 600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.current_project = None # Initialize current_project to None

        self.setup_screens()
        self.splash_screen.finish(self)

    def setup_screens(self):
        # Create screen instances
        self.loading_screen_widget = LoadingScreenWidget(self)
        self.main_menu_screen = MainMenuScreen(self)
        self.new_project_screen = NewProjectScreen(self)
        self.category1_screen = Category1Screen(self)

        # Add screens to stacked widget
        self.stacked_widget.addWidget(self.loading_screen_widget) # Index 0
        self.stacked_widget.addWidget(self.main_menu_screen)      # Index 1
        self.stacked_widget.addWidget(self.new_project_screen)    # Index 2
        self.stacked_widget.addWidget(self.category1_screen)      # Index 3
        # self.stacked_widget.addWidget(self.category2_screen)
        # self.stacked_widget.addWidget(self.element_management_screen)
        # self.stacked_widget.addWidget(self.reinforcement_screen)

        # Set initial screen
        self.go_to_main_menu_screen()

    def go_to_main_menu_screen(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_new_project_screen(self):
        self.stacked_widget.setCurrentIndex(2)

    def go_to_category1_screen(self):
        self.stacked_widget.setCurrentIndex(3)

    # def go_to_category2_screen(self):
    #     self.stacked_widget.setCurrentWidget(self.category2_screen)

    # def go_to_element_management_screen(self):
    #     self.stacked_widget.setCurrentWidget(self.element_management_screen)

    # def go_to_reinforcement_screen(self):
    #     self.stacked_widget.setCurrentWidget(self.reinforcement_screen)


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
