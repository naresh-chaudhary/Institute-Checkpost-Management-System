# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created: Tue Apr 14 21:40:25 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore, QtGui
import sys
import data_entry,queries
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

class Ui_Options_form(QtGui.QWidget):
    flag=0
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.confirm=None
    def setupUi(self, Options_form):
        Options_form.setObjectName(_fromUtf8("Options_form"))
        Options_form.resize(475, 291)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Options_form.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        Options_form.setFont(font)
        Options_form.setStyleSheet(_fromUtf8("#Options_form{\n"
"background-image: url(/Python27/ICPMS/options3.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: 250px 250px;\n"
"background-color:white;\n"
"}\n"
"QPushButton {\n"
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
"max-height: 20px;\n"
"}\n"
""))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Options_form)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Options_form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NEOTERIQUE"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        self.dataentry_rbtn = QtGui.QRadioButton(Options_form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dataentry_rbtn.setFont(font)
        self.dataentry_rbtn.setStyleSheet(_fromUtf8(""))
        self.dataentry_rbtn.setObjectName(_fromUtf8("dataentry_rbtn"))
        self.buttonGroup = QtGui.QButtonGroup(Options_form)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.dataentry_rbtn)
        self.horizontalLayout.addWidget(self.dataentry_rbtn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.queries_rbtn = QtGui.QRadioButton(Options_form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.queries_rbtn.setFont(font)
        self.queries_rbtn.setObjectName(_fromUtf8("queries_rbtn"))
        self.buttonGroup.addButton(self.queries_rbtn)
        self.horizontalLayout.addWidget(self.queries_rbtn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.ok_btn = QtGui.QPushButton(Options_form)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet(_fromUtf8("width:70px"))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.horizontalLayout_2.addWidget(self.ok_btn)
        self.cancel_btn = QtGui.QPushButton(Options_form)
        self.cancel_btn.setMinimumSize(QtCore.QSize(82, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(_fromUtf8("width:70px"))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.que=queries.Ui_queries()
        self.dat=data_entry.Ui_Form()
        
        self.connect(self.dataentry_rbtn, QtCore.SIGNAL("toggled(bool)"),self.setflag1)
        self.connect(self.queries_rbtn,QtCore.SIGNAL("toggled(bool)"),self.setflag2)
        self.connect(self.ok_btn, QtCore.SIGNAL("clicked()"),self.checkflag)
        self.connect(self.cancel_btn,QtCore.SIGNAL("clicked()"),self.close)

        self.retranslateUi(Options_form)
        QtCore.QMetaObject.connectSlotsByName(Options_form)

    def setflag1(self,flag):
        self.flag=1

    def setflag2(self,flag):
        self.flag=2
        
    def checkflag(self):
        if self.flag==1:
            self.dat.show()
            self.close()
        elif self.flag==2:
            self.que.show()
            self.close()

    def retranslateUi(self, Options_form):
        Options_form.setWindowTitle(_translate("Options_form", "Form", None))
        self.label.setText(_translate("Options_form", "What would you like to do??", None))
        self.dataentry_rbtn.setText(_translate("Options_form", "Data Entry", None))
        self.queries_rbtn.setText(_translate("Options_form", "Queries", None))
        self.ok_btn.setText(_translate("Options_form", "OK", None))
        self.cancel_btn.setText(_translate("Options_form", "Cancel", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Options_form = QtGui.QWidget()
    ui = Ui_Options_form()
    ui.setupUi(Options_form)
    Options_form.show()
    sys.exit(app.exec_())


