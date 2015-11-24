# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_by_name.ui'
#
# Created: Mon Apr 13 23:08:11 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import queries,DB_manager,data_retreived

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

class Ui_Dialog(QtGui.QDialog):
    def __init__(self,date):
        QtGui.QDialog.__init__(self)
        self.date=date
        self.setupUi(self)
        self.confirm=None
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(617, 358)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"background-image: url(C:/Python27/ICPMS/search.png);\n"
"background-repeat:no repeat;\n"
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
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(295, 10, 301, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NEOTERIQUE"))
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 240, 341, 91))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Fname_lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.Fname_lineEdit.setStyleSheet(_fromUtf8("QLineEdit{\n"
"\n"
"}"))
        self.Fname_lineEdit.setText(_fromUtf8(""))
        self.Fname_lineEdit.setObjectName(_fromUtf8("Fname_lineEdit"))
        self.horizontalLayout.addWidget(self.Fname_lineEdit)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.Lname_lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.Lname_lineEdit.setObjectName(_fromUtf8("Lname_lineEdit"))
        self.horizontalLayout.addWidget(self.Lname_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ok_btn = QtGui.QPushButton(self.layoutWidget1)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.horizontalLayout_2.addWidget(self.ok_btn)
        self.back_btn = QtGui.QPushButton(self.layoutWidget1)
        self.back_btn.setObjectName(_fromUtf8("back_btn"))
        self.horizontalLayout_2.addWidget(self.back_btn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.back_clicked)
        QtCore.QObject.connect(self.ok_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ok_clicked)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ok_clicked(self):
        self.Fname=self.Fname_lineEdit.text()
        self.Lname=self.Lname_lineEdit.text()
        self.dbu=DB_manager.DatabaseUtility('icpms','person','vehicle','purpose')
        
        if self.Lname=='' and self.Fname=='':
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Both fields can\'nt be left blank simultaneously!!')
        elif self.Lname=='':
            table=self.dbu.GetByFname(self.Fname,self.date)
            self.dr=data_retreived.Ui_Form(table)
            self.dr.show()
            self.close()
        elif self.Fname=='':
            table=self.dbu.GetByLname(self.Lname,self.date)
            self.dr=data_retreived.Ui_Form(table)
            self.dr.show()
            self.close()
        else:
            table=self.dbu.GetByName(self.Fname,self.Lname,self.date)
            self.dr=data_retreived.Ui_Form(table)
            self.dr.show()
            self.close()     
        
    def back_clicked(self):
        self.q=queries.Ui_queries()
        self.q.show()
        self.close()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Search by Name", None))
        self.Fname_lineEdit.setPlaceholderText(_translate("Dialog", "First Name", None))
        self.label_2.setText(_translate("Dialog", "OR", None))
        self.Lname_lineEdit.setPlaceholderText(_translate("Dialog", "Last Name", None))
        self.ok_btn.setText(_translate("Dialog", "OK", None))
        self.back_btn.setText(_translate("Dialog", "Back", None))
        self.label.setText(_translate("Dialog", "Enter First Name or Last Name", None))

'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Dialog(12)
    ui.show()
    sys.exit(app.exec_())
'''

