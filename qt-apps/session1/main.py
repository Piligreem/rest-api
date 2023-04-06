from PyQt5 import QtWidgets, QtCore
# Импортируем наш файл
from ui.start_window import Ui_MainWindow
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.init_slots()

    def init_slots(self):
        self.pers_visit_form = QtWidgets.QWidget()
        self.group_visit_form = QtWidgets.QWidget()
        self.pers_visit_form = self._ui.get_personal_visit_window(self.pers_visit_form)
        self.group_visit_form = self._ui.get_group_visit_window(self.group_visit_form)
        self._ui.pushButton.clicked.connect(self.pers_visit_form.show)
        self._ui.pushButton_2.clicked.connect(self.group_visit_form.show)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())

