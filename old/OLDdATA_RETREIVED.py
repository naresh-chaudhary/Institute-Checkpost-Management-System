# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_retreived.ui'
#
# Created: Sun Apr 12 01:42:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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
    def __init__(self,table):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.table=table
        self.confirm=None
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1000, 700)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NEOTERIQUE"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ZOMBIFIED"))
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.ok_btn_clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #self.dbu=DB_manager.DatabaseUtility('testing','person','vehicle','purpose')
        #col1 = self.dbu.GetColumns1()
        #col2 = self.dbu.GetColumns2()
        #table= self.dbu.GetTable1joinTable2()
        
        #table1 = self.dbu.GetTable1()
        #table2 = self.dbu.GetTable2()
        #table=table1+table2
        #print table
        
        '''for c in range(len(col)):
            self.treeWidget.headerItem().setText(c, col[c][0])'''
        
        self.treeWidget.clear()
        
        for item in range(len(self.table)):
            QtGui.QTreeWidgetItem(self.treeWidget)
            for value in range(len(self.table[item])):
                self.treeWidget.topLevelItem(item).setText(value, str(self.table[item][value]))

    def ok_btn_clicked(self):
        self.close()
                
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ICPMS", None))
        self.label.setText(_translate("Form", "Data Retreived", None))
        self.label_2.setText(_translate("Form", "date", None))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Fname", None))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Lname", None))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Sex", None))
        self.treeWidget.headerItem().setText(3, _translate("Form", "Address", None))
        self.treeWidget.headerItem().setText(4, _translate("Form", "Id_type", None))
        self.treeWidget.headerItem().setText(5, _translate("Form", "Id_No", None))
        self.treeWidget.headerItem().setText(6, _translate("Form", "New Column", None))
        self.treeWidget.headerItem().setText(7, _translate("Form", "Vehicle", None))
        self.treeWidget.headerItem().setText(8, _translate("Form", "Vehicle_no", None))
        self.treeWidget.headerItem().setText(9, _translate("Form", "Landline", None))
        self.pushButton.setText(_translate("Form", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())

