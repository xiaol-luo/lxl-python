
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        import qt_ui.main_dialog
        self.ui = qt_ui.main_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self._clicked_ok)
    
    def _clicked_ok(self):
        print("clicked ok")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        import qt_ui.main_window
        self.ui = qt_ui.main_dialog.main_window.Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_dialog = MainDialog()
    my_dialog.show()
    sys.exit(app.exec_())