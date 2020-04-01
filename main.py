from PySide2 import QtCore, QtGui, QtWidgets
from covid import Ui_Form
import sys

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

sys.exit(app.exec_())
