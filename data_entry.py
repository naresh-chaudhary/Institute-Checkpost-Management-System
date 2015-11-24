# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_entry.ui'
#
# Created: Tue Apr 14 21:32:53 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import DB_manager,purpose,options
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
    flag_id=0
    flag_sex=0
    vehicle_type=0
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.confirm=None
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(794, 668)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setStyleSheet(_fromUtf8("#Form{\n"
"background-image: url(C:/Python27/ICPMS/data3.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: top right;\n"
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
"QLineEdit{\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"width:250px;\n"
"height:20px;\n"                                    
"}\n"
"\n"
"QComboBox{\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"width:245px;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Lname_lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lname_lineEdit.sizePolicy().hasHeightForWidth())
        self.Lname_lineEdit.setSizePolicy(sizePolicy)
        self.Lname_lineEdit.setStyleSheet(_fromUtf8(""))
        self.Lname_lineEdit.setObjectName(_fromUtf8("Lname_lineEdit"))
        self.gridLayout.addWidget(self.Lname_lineEdit, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setUnderline(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.std_id_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.std_id_rbtn.setFont(font)
        self.std_id_rbtn.setMouseTracking(True)
        self.std_id_rbtn.setObjectName(_fromUtf8("std_id_rbtn"))
        self.buttonGroup_2 = QtGui.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.std_id_rbtn)
        self.horizontalLayout.addWidget(self.std_id_rbtn)
        self.staff_id_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.staff_id_rbtn.setFont(font)
        self.staff_id_rbtn.setObjectName(_fromUtf8("staff_id_rbtn"))
        self.buttonGroup_2.addButton(self.staff_id_rbtn)
        self.horizontalLayout.addWidget(self.staff_id_rbtn)
        self.other_id_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.other_id_rbtn.setFont(font)
        self.other_id_rbtn.setObjectName(_fromUtf8("other_id_rbtn"))
        self.buttonGroup_2.addButton(self.other_id_rbtn)
        self.horizontalLayout.addWidget(self.other_id_rbtn)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 2, 1, 1)
        self.adddress_lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adddress_lineEdit.sizePolicy().hasHeightForWidth())
        self.adddress_lineEdit.setSizePolicy(sizePolicy)
        self.adddress_lineEdit.setStyleSheet(_fromUtf8("width:250px"))
        self.adddress_lineEdit.setObjectName(_fromUtf8("adddress_lineEdit"))
        self.gridLayout.addWidget(self.adddress_lineEdit, 4, 2, 1, 1)
        self.Fname_lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fname_lineEdit.sizePolicy().hasHeightForWidth())
        self.Fname_lineEdit.setSizePolicy(sizePolicy)
        self.Fname_lineEdit.setStyleSheet(_fromUtf8("width:250px"))
        self.Fname_lineEdit.setObjectName(_fromUtf8("Fname_lineEdit"))
        self.gridLayout.addWidget(self.Fname_lineEdit, 1, 2, 1, 1)
        self.vehicletype_comboBox = QtGui.QComboBox(Form)
        self.vehicletype_comboBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vehicletype_comboBox.sizePolicy().hasHeightForWidth())
        self.vehicletype_comboBox.setSizePolicy(sizePolicy)
        self.vehicletype_comboBox.setStyleSheet(_fromUtf8("border-radius:10px;width:245px"))
        self.vehicletype_comboBox.setObjectName(_fromUtf8("vehicletype_comboBox"))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.vehicletype_comboBox, 8, 2, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 9, 1, 1, 1)
        self.vehicle_number_lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vehicle_number_lineEdit.sizePolicy().hasHeightForWidth())
        self.vehicle_number_lineEdit.setSizePolicy(sizePolicy)
        self.vehicle_number_lineEdit.setObjectName(_fromUtf8("vehicle_number_lineEdit"))
        self.gridLayout.addWidget(self.vehicle_number_lineEdit, 9, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 8, 1, 1, 1)
        self.idnumber_lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idnumber_lineEdit.sizePolicy().hasHeightForWidth())
        self.idnumber_lineEdit.setSizePolicy(sizePolicy)
        self.idnumber_lineEdit.setObjectName(_fromUtf8("idnumber_lineEdit"))
        self.gridLayout.addWidget(self.idnumber_lineEdit, 7, 2, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 10, 1, 1, 1)
        self.other_lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_lineEdit.sizePolicy().hasHeightForWidth())
        self.other_lineEdit.setSizePolicy(sizePolicy)
        self.other_lineEdit.setStyleSheet(_fromUtf8(""))
        self.other_lineEdit.setText(_fromUtf8(""))
        self.other_lineEdit.setObjectName(_fromUtf8("other_lineEdit"))
        self.gridLayout.addWidget(self.other_lineEdit, 6, 2, 1, 1)
        self.contact_lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contact_lineEdit.sizePolicy().hasHeightForWidth())
        self.contact_lineEdit.setSizePolicy(sizePolicy)
        self.contact_lineEdit.setMaxLength(10)
        self.contact_lineEdit.setObjectName(_fromUtf8("contact_lineEdit"))
        self.gridLayout.addWidget(self.contact_lineEdit, 10, 2, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 13, 1, 1, 1)
        self.label_10 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 11, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 11, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.ok_btn = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.horizontalLayout_3.addWidget(self.ok_btn)
        self.cancel_btn = QtGui.QPushButton(Form)
        self.cancel_btn.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 12, 1, 1, 2)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 6, 3, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.female_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.female_rbtn.setFont(font)
        self.female_rbtn.setObjectName(_fromUtf8("female_rbtn"))
        self.buttonGroup = QtGui.QButtonGroup(Form)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.female_rbtn)
        self.horizontalLayout_2.addWidget(self.female_rbtn)
        self.male_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.male_rbtn.setFont(font)
        self.male_rbtn.setObjectName(_fromUtf8("male_rbtn"))
        self.buttonGroup.addButton(self.male_rbtn)
        self.horizontalLayout_2.addWidget(self.male_rbtn)
        self.other_sex_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.other_sex_rbtn.setFont(font)
        self.other_sex_rbtn.setObjectName(_fromUtf8("other_sex_rbtn"))
        self.buttonGroup.addButton(self.other_sex_rbtn)
        self.horizontalLayout_2.addWidget(self.other_sex_rbtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancel_clicked)
        QtCore.QObject.connect(self.std_id_rbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_7.hide)
        QtCore.QObject.connect(self.other_id_rbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_7.show)
        QtCore.QObject.connect(self.staff_id_rbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.other_lineEdit.hide)
        QtCore.QObject.connect(self.std_id_rbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.other_lineEdit.hide)
        QtCore.QObject.connect(self.other_id_rbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.other_lineEdit.show)
        QtCore.QObject.connect(self.staff_id_rbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_7.hide)
        QtCore.QObject.connect(self.ok_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ok_clicked)
        QtCore.QObject.connect(self.std_id_rbtn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.set_id_flag1)
        QtCore.QObject.connect(self.staff_id_rbtn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.set_id_flag2)
        QtCore.QObject.connect(self.other_id_rbtn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.set_id_flag3)
        QtCore.QObject.connect(self.male_rbtn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.set_sex_flag1)
        QtCore.QObject.connect(self.female_rbtn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.set_sex_flag2)
        QtCore.QObject.connect(self.other_sex_rbtn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.set_sex_flag3)
        QtCore.QObject.connect(self.vehicletype_comboBox,QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.set_vtype)
        
        QtCore.QMetaObject.connectSlotsByName(Form)
    def cancel_clicked(self):
        self.o=options.Ui_Options_form()
        self.o.show()
        self.close()
        
        
    def set_vtype(self):
        self.vehicle_type=self.vehicletype_comboBox.currentText()
    def set_sex_flag1(self):
        self.flag_sex=1
    def set_sex_flag2(self):
        self.flag_sex=2
    def set_sex_flag3(self):
        self.flag_sex=3
        
    def set_id_flag1(self):
        self.flag_id=1

    def set_id_flag2(self):
        self.flag_id=2
        
    def set_id_flag3(self):
        self.flag_id=3
        
    def ok_clicked(self):
        self.fname=self.Fname_lineEdit.text()
        self.sex='NA'
        self.id_type='NA'
        if self.flag_sex==3:
            self.sex='other'
        elif self.flag_sex==2:
            self.sex='female'
        elif self.flag_sex==1:
            self.sex='male'
        else:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Sex Missing!')
        if not self.fname:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'First Name Missing!')
        self.lname=self.Lname_lineEdit.text()
        if not self.lname:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Last Name Missing!')
        self.address=self.adddress_lineEdit.text()
        if not self.address:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Address Missing!')
        if self.flag_id==3:
            self.id_type=self.other_lineEdit.text()
        elif self.flag_id==2:
            self.id_type='Staff Id'
        elif self.flag_id==1:
            self.id_type='Student Id'
        else:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Id type Missing!')
        self.id_no=self.idnumber_lineEdit.text()
        if not self.id_no:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Id Number Missing!')
        self.mobile_no=self.contact_lineEdit.text()
        self.landline=self.lineEdit.text()
        self.vehicle_no=self.vehicle_number_lineEdit.text()
        if not self.vehicle_no:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Vehicle number Missing!')
        #self.vehicle_type=self.vehicletype_comboBox.text()
        if not self.vehicle_type:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'vehicle type Missing!')
        
        dbu=DB_manager.DatabaseUtility('icpms','person','vehicle','purpose')
        dbu.AddEntryToTable1(self.id_no,self.id_type,self.fname,self.lname,self.sex,self.address,self.mobile_no,self.landline)
        if self.vehicle_type  != 'Pedestrian':
            dbu.AddEntryToTable2(self.id_no,self.vehicle_no,self.vehicle_type)
        if self.flag_id==3:
            self.d=dbu.date1
            self.t=dbu.time
            self.p=purpose.Ui_Form(self.id_no,self.d,self.t)
            self.p.show()
        QtGui.QMessageBox.information(self, 'Congrats!!', 'Data successfully saved!')
        

    

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Lname_lineEdit.setPlaceholderText(_translate("Form", "   Last Name", None))
        self.label_6.setText(_translate("Form", "Sex", None))
        self.label_9.setText(_translate("Form", "Address", None))
        self.label_2.setText(_translate("Form", "ID Type", None))
        self.std_id_rbtn.setText(_translate("Form", "Student ID", None))
        self.staff_id_rbtn.setText(_translate("Form", "Staff Id", None))
        self.other_id_rbtn.setText(_translate("Form", "Other", None))
        self.Fname_lineEdit.setPlaceholderText(_translate("Form", "   First Name", None))
        self.vehicletype_comboBox.setItemText(0, _translate("Form", "--SELECT--", None))
        self.vehicletype_comboBox.setItemText(1, _translate("Form", "Pedestrian", None))
        self.vehicletype_comboBox.setItemText(2, _translate("Form", "Motorcylcle", None))
        self.vehicletype_comboBox.setItemText(3, _translate("Form", "Scooter", None))
        self.vehicletype_comboBox.setItemText(4, _translate("Form", "Car", None))
        self.vehicletype_comboBox.setItemText(5, _translate("Form", "Truck", None))
        self.vehicletype_comboBox.setItemText(6, _translate("Form", "Rikshaw", None))
        self.vehicletype_comboBox.setItemText(7, _translate("Form", "Van", None))
        self.vehicletype_comboBox.setItemText(8, _translate("Form", "Tractor", None))
        self.vehicletype_comboBox.setItemText(9, _translate("Form", "Bus", None))
        self.label_7.setText(_translate("Form", "In case of other, please specify:", None))
        self.label_4.setText(_translate("Form", "Vehicle Number", None))
        self.label_3.setText(_translate("Form", "Vehicle Type", None))
        self.label_5.setText(_translate("Form", "Mobile No.", None))
        self.contact_lineEdit.setPlaceholderText(_translate("Form", "max. 10 digits are allowed", None))
        self.label_8.setText(_translate("Form", "ID Number", None))
        self.label.setText(_translate("Form", "Name", None))
        self.label_10.setText(_translate("Form", "Landline No.", None))
        self.ok_btn.setText(_translate("Form", "OK", None))
        self.cancel_btn.setText(_translate("Form", "BACK", None))
        self.female_rbtn.setText(_translate("Form", "Female", None))
        self.male_rbtn.setText(_translate("Form", "Male", None))
        self.other_sex_rbtn.setText(_translate("Form", "Other", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

