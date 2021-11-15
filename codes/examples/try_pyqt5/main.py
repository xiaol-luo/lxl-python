
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        import qt_ui.main_widget
        self.ui = qt_ui.main_widget.Ui_Form()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self._clicked_ok)

    def _clicked_ok(self):
        print("MainWidget clicked ok")


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        import qt_ui.main_dialog
        self.ui = qt_ui.main_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self._clicked_ok)
    
    def _clicked_ok(self):
        print("MainDialog clicked ok")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        import qt_ui.main_window
        self.ui = qt_ui.main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_tab_1.clicked.connect(self._on_click_btn_tab_1)
        self.ui.btn_tab_2.clicked.connect(self._on_click_btn_tab_2)
        self.ui.btn_tab_3.clicked.connect(self._on_click_btn_tab_3)
        self.main_dialog = MainDialog(self)
        self.main_widget = MainWidget(self.ui.widget_holder)
    
    def _on_click_btn_tab_1(self):
        self.main_dialog.open()
        print("_on_click_btn_tab_1")

    def _on_click_btn_tab_2(self):
        print("_on_click_btn_tab_1")
        
    def _on_click_btn_tab_3(self):
        print("_on_click_btn_tab_1")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MainWindow()
    my_window.show()
    sys.exit(app.exec_())