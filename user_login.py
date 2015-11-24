#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'user_login.ui'
#
# Created: Tue Apr 14 21:52:43 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import options
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.confirm = None  
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(551, 265)
        Form.setStyleSheet(_fromUtf8("#Form{\n"
"background-image: url(C:/Python27/ICPMS/login.jpg);\n"
"background-repeat:no repeat;\n"
"background-position:left;\n"
"background-color:white;\n"
"}\n"
"QPushButton{\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 18px;\n"
"max-height: 20px;}\n"
"\n"
"QLineEdit{\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
""))
        self.cancel_btn = QtGui.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(450, 210, 84, 28))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        self.cancel_btn.setMinimumSize(QtCore.QSize(84, 26))
        self.cancel_btn.setStyleSheet(_fromUtf8("width:72px"))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.login_btn = QtGui.QPushButton(Form)
        self.login_btn.setGeometry(QtCore.QRect(330, 210, 84, 28))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(84, 26))
        self.login_btn.setStyleSheet(_fromUtf8("width:72px"))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(240, 130, 293, 60))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.username_label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_label.setFont(font)
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.horizontalLayout.addWidget(self.username_label)
        self.username_lineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_lineEdit.sizePolicy().hasHeightForWidth())
        self.username_lineEdit.setSizePolicy(sizePolicy)
        self.username_lineEdit.setStyleSheet(_fromUtf8("width:200px"))
        self.username_lineEdit.setObjectName(_fromUtf8("username_lineEdit"))
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.password_label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.horizontalLayout_2.addWidget(self.password_label)
        self.password_lineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lineEdit.sizePolicy().hasHeightForWidth())
        self.password_lineEdit.setSizePolicy(sizePolicy)
        self.password_lineEdit.setStyleSheet(_fromUtf8("width:200px"))
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 501, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NEOTERIQUE"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        QtCore.QObject.connect(self.login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Login_btn)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.cancel_btn.setText(_translate("Form", "Cancel", None))
        self.login_btn.setText(_translate("Form", "Login", None))
        self.username_label.setText(_translate("Form", "Username", None))
        self.password_label.setText(_translate("Form", "Password", None))
        self.label.setText(_translate("Form", "INSTITUTE CHECKPOST MANAGEMENT SYSTEM", None))

    def Login_btn(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        if not username:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Username Missing!')
        elif not password:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
        else:
            self.AttemptLogin(username, password)

    def AttemptLogin(self, username, password):
         
        if username == 'admin':
            if password == '12345':
                self.options=options.Ui_Options_form()
                self.options.show()
                self.close()
        else:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
            return



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

