import sys
import user_login
from PyQt4 import QtGui,QtCore

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = user_login.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
