# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_entry.ui'
#
# Created: Thu Apr 09 23:09:55 2015
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
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(794, 622)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setMargin(9)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dataentry_lbl = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NEOTERIQUE"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.dataentry_lbl.setFont(font)
        self.dataentry_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.dataentry_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.dataentry_lbl.setObjectName(_fromUtf8("dataentry_lbl"))
        self.verticalLayout.addWidget(self.dataentry_lbl, QtCore.Qt.AlignHCenter)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout.setLayout(1, QtGui.QFormLayout.SpanningRole, self.verticalLayout)
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
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.label_6 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.male_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.male_rbtn.setFont(font)
        self.male_rbtn.setObjectName(_fromUtf8("male_rbtn"))
        self.horizontalLayout_2.addWidget(self.male_rbtn)
        self.female_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.female_rbtn.setFont(font)
        self.female_rbtn.setObjectName(_fromUtf8("female_rbtn"))
        self.horizontalLayout_2.addWidget(self.female_rbtn)
        self.other_sex_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.other_sex_rbtn.setFont(font)
        self.other_sex_rbtn.setObjectName(_fromUtf8("other_sex_rbtn"))
        self.horizontalLayout_2.addWidget(self.other_sex_rbtn)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_9 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setUnderline(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_9)
        self.adddress_lineEdit = QtGui.QLineEdit(Form)
        self.adddress_lineEdit.setObjectName(_fromUtf8("adddress_lineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.adddress_lineEdit)
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.std_id_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.std_id_rbtn.setFont(font)
        self.std_id_rbtn.setMouseTracking(True)
        self.std_id_rbtn.setObjectName(_fromUtf8("std_id_rbtn"))
        self.horizontalLayout.addWidget(self.std_id_rbtn)
        self.staff_id_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.staff_id_rbtn.setFont(font)
        self.staff_id_rbtn.setObjectName(_fromUtf8("staff_id_rbtn"))
        self.horizontalLayout.addWidget(self.staff_id_rbtn)
        self.other_id_rbtn = QtGui.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.other_id_rbtn.setFont(font)
        self.other_id_rbtn.setObjectName(_fromUtf8("other_id_rbtn"))
        self.horizontalLayout.addWidget(self.other_id_rbtn)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.other_lineEdit = QtGui.QLineEdit(Form)
        self.other_lineEdit.setText(_fromUtf8(""))
        self.other_lineEdit.setObjectName(_fromUtf8("other_lineEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.other_lineEdit)
        self.label_8 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_8)
        self.idnumber_lineEdit = QtGui.QLineEdit(Form)
        self.idnumber_lineEdit.setObjectName(_fromUtf8("idnumber_lineEdit"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.idnumber_lineEdit)
        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_3)
        self.vehicletype_comboBox = QtGui.QComboBox(Form)
        self.vehicletype_comboBox.setEnabled(True)
        self.vehicletype_comboBox.setObjectName(_fromUtf8("vehicletype_comboBox"))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.vehicletype_comboBox.addItem(_fromUtf8(""))#by me
        self.vehicletype_comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.vehicletype_comboBox)
        self.label_4 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.label_4)
        self.vehicle_number_lineEdit = QtGui.QLineEdit(Form)
        self.vehicle_number_lineEdit.setObjectName(_fromUtf8("vehicle_number_lineEdit"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.vehicle_number_lineEdit)
        self.label_5 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.LabelRole, self.label_5)
        self.contact_lineEdit = QtGui.QLineEdit(Form)
        self.contact_lineEdit.setMaxLength(10)
        self.contact_lineEdit.setObjectName(_fromUtf8("contact_lineEdit"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.contact_lineEdit)
        self.label_10 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.ok_btn = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ZOMBIFIED"))
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.horizontalLayout_3.addWidget(self.ok_btn)
        self.cancel_btn = QtGui.QPushButton(Form)
        self.cancel_btn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ZOMBIFIED"))
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.formLayout.setLayout(18, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.Fname_lineEdit = QtGui.QLineEdit(Form)
        self.Fname_lineEdit.setObjectName(_fromUtf8("Fname_lineEdit"))
        self.horizontalLayout_5.addWidget(self.Fname_lineEdit)
        self.Lname_lineEdit = QtGui.QLineEdit(Form)
        self.Lname_lineEdit.setObjectName(_fromUtf8("Lname_lineEdit"))
        self.horizontalLayout_5.addWidget(self.Lname_lineEdit)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.formLayout)

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
        self.close()
        
        
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ICPMS", None))
        self.dataentry_lbl.setText(_translate("Form", "DATA ENTRY", None))
        self.label.setText(_translate("Form", "Name", None))
        self.label_6.setText(_translate("Form", "Sex", None))
        self.male_rbtn.setText(_translate("Form", "MALE", None))
        self.female_rbtn.setText(_translate("Form", "FEMALE", None))
        self.other_sex_rbtn.setText(_translate("Form", "OTHER", None))
        self.label_9.setText(_translate("Form", "Address", None))
        self.label_2.setText(_translate("Form", "ID Type", None))
        self.std_id_rbtn.setText(_translate("Form", "STUDENT ID", None))
        self.staff_id_rbtn.setText(_translate("Form", "STAFF ID", None))
        self.other_id_rbtn.setText(_translate("Form", "OTHER", None))
        self.label_7.setText(_translate("Form", "In case of other, please specify:", None))
        self.label_8.setText(_translate("Form", "ID Number", None))
        self.label_3.setText(_translate("Form", "Vehicle Type", None))
        self.vehicletype_comboBox.setItemText(0, _translate("Form", "--SELECT--", None))
        self.vehicletype_comboBox.setItemText(1, _translate("Form", "Pedestrian", None))
        self.vehicletype_comboBox.setItemText(2, _translate("Form", "Motorcycle", None))
        self.vehicletype_comboBox.setItemText(3, _translate("Form", "Scooter", None))
        self.vehicletype_comboBox.setItemText(4, _translate("Form", "Car", None))
        self.vehicletype_comboBox.setItemText(5, _translate("Form", "Truck", None))
        self.vehicletype_comboBox.setItemText(6, _translate("Form", "Rikshaw", None))
        self.vehicletype_comboBox.setItemText(7, _translate("Form", "Van", None))
        self.vehicletype_comboBox.setItemText(8, _translate("Form", "Tractor", None))
        self.vehicletype_comboBox.setItemText(9, _translate("Form", "Bus", None))
        self.label_4.setText(_translate("Form", "Vehicle Number", None))
        self.label_5.setText(_translate("Form", "Mobile No.", None))
        self.contact_lineEdit.setPlaceholderText(_translate("Form", "max. 10 digits are allowed", None))
        self.label_10.setText(_translate("Form", "Landline No.", None))
        self.ok_btn.setText(_translate("Form", "OK", None))
        self.cancel_btn.setText(_translate("Form", "BACK", None))
        self.Fname_lineEdit.setPlaceholderText(_translate("Form", "   First Name", None))
        self.Lname_lineEdit.setPlaceholderText(_translate("Form", "   Last Name", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())

