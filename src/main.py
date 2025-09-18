from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication([])

loader = QUiLoader()
list_of_files = ["assets/ui/GenBBS_loading.ui", "assets/ui/GenBBS_catg2.ui", "assets/ui/GenBBS_catg1.ui", "assets/ui/GenBBS.ui", "assets/ui/GenBBS_element.ui", "assets/ui/GenBBS_reinf.ui"]
ui_file = QFile(list_of_files[3])
ui_file.open(QFile.ReadOnly)
window = loader.load(ui_file)
ui_file.close()

window.show()

app.exec()
