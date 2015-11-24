# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created: Wed Apr 08 01:53:15 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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
        Options_form.resize(400, 291)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Options_form.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        Options_form.setFont(font)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Options_form)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(Options_form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NEOTERIQUE"))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.dataentry_rbtn = QtGui.QRadioButton(Options_form)
        self.dataentry_rbtn.setObjectName(_fromUtf8("dataentry_rbtn"))
        self.horizontalLayout.addWidget(self.dataentry_rbtn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.update_rbtn = QtGui.QRadioButton(Options_form)
        self.update_rbtn.setObjectName(_fromUtf8("update_rbtn"))
        self.horizontalLayout.addWidget(self.update_rbtn)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.queries_rbtn = QtGui.QRadioButton(Options_form)
        self.queries_rbtn.setObjectName(_fromUtf8("queries_rbtn"))
        self.horizontalLayout.addWidget(self.queries_rbtn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.ok_btn = QtGui.QPushButton(Options_form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ZOMBIFIED"))
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.horizontalLayout_2.addWidget(self.ok_btn)
        self.cancel_btn = QtGui.QPushButton(Options_form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ZOMBIFIED"))
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.que=queries.Ui_queries()
        self.dat=data_entry.Ui_Form()
        
        self.connect(self.dataentry_rbtn, QtCore.SIGNAL("toggled(bool)"),self.setflag1)
        self.connect(self.queries_rbtn,QtCore.SIGNAL("toggled(bool)"),self.setflag2)
        self.connect(self.update_rbtn,QtCore.SIGNAL("toggled(bool)"),self.setflag3)
        self.connect(self.ok_btn, QtCore.SIGNAL("clicked()"),self.checkflag)
        self.connect(self.cancel_btn,QtCore.SIGNAL("clicked()"),self.close)

        
        self.retranslateUi(Options_form)
        QtCore.QMetaObject.connectSlotsByName(Options_form)


    def setflag1(self,flag):
        self.flag=1

    def setflag2(self,flag):
        self.flag=2
    def setflag3(self,flag):
        pass
        
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
        self.update_rbtn.setText(_translate("Options_form", "Update", None))
        self.queries_rbtn.setText(_translate("Options_form", "Queries", None))
        self.ok_btn.setText(_translate("Options_form", "OK", None))
        self.cancel_btn.setText(_translate("Options_form", "Cancel", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Options_form()
    ui.show()
    sys.exit(app.exec_())

