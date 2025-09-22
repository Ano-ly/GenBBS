from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QSplashScreen, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter
import resources

# --- Screen Classes (will eventually be in separate files) ---
class LoadingScreenWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_loading.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

class MainMenuScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loaded_ui = QUiLoader().load("assets/ui/GenBBS.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(self.loaded_ui)
        self.setLayout(layout)
        self.connect_buttons()

    def connect_buttons(self):
        new_project_button = self.loaded_ui.findChild(QPushButton, "crNewFile")
        if new_project_button:
            new_project_button.clicked.connect(self.parent().go_to_new_project_screen)

        existing_file_button = self.loaded_ui.findChild(QPushButton, "crExistingFile")
        if existing_file_button:
            existing_file_button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open Existing Project")
        file_dialog.setNameFilter("GenBBS Project Files (*.genbbs)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            print(f"Selected file: {selected_file}")
            # TODO: Implement logic to load the selected project file

class NewProjectScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loaded_ui = QUiLoader().load("assets/ui/GenBBS_newprj.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(self.loaded_ui)
        self.setLayout(layout)
        self.connect_buttons()

    def connect_buttons(self):
        back_button = self.loaded_ui.findChild(QPushButton, "btnBackNewprj")
        if back_button:
            back_button.clicked.connect(self.parent().go_to_main_menu_screen)

class Category1Screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_catg1.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

class Category2Screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_catg2.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

class ElementManagementScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loaded_ui = QUiLoader().load("assets/ui/GenBBS_element.ui")
        layout = QVBoxLayout(self)
        layout.addWidget(loaded_ui)
        self.setLayout(layout)

class ReinforcementScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
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

        self.setup_screens()
        self.splash_screen.finish(self)

    def setup_screens(self):
        # Create screen instances
        self.loading_screen_widget = LoadingScreenWidget(self)
        self.main_menu_screen = MainMenuScreen(self)
        self.new_project_screen = NewProjectScreen(self)
        self.category1_screen = Category1Screen(self)
        self.category2_screen = Category2Screen(self)
        self.element_management_screen = ElementManagementScreen(self)
        self.reinforcement_screen = ReinforcementScreen(self)

        # Add screens to the stacked widget
        self.stacked_widget.addWidget(self.loading_screen_widget)
        self.stacked_widget.addWidget(self.main_menu_screen)
        self.stacked_widget.addWidget(self.new_project_screen)
        self.stacked_widget.addWidget(self.category1_screen)
        self.stacked_widget.addWidget(self.category2_screen)
        self.stacked_widget.addWidget(self.element_management_screen)
        self.stacked_widget.addWidget(self.reinforcement_screen)

        # Set initial screen to MainMenuScreen after splash screen
        self.stacked_widget.setCurrentWidget(self.main_menu_screen)

    # New navigation methods
    def go_to_main_menu_screen(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_screen)

    def go_to_new_project_screen(self):
        self.stacked_widget.setCurrentWidget(self.new_project_screen)

    # Removed direct navigation methods for other screens as they are not directly accessible from main menu
    # def go_to_category1_screen(self):
    #     self.stacked_widget.setCurrentWidget(self.category1_screen)

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
