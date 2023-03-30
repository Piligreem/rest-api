from PyQt5 import QtWidgets, uic

# import icons_rc

gui = QtWidgets.QApplication([])
ui=uic.loadUi('ui/session1.ui')

ui.show()
gui.exec()
