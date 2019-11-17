# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(737, 417)
        self.UpdateButton = QtWidgets.QPushButton(Form)
        self.UpdateButton.setGeometry(QtCore.QRect(500, 160, 171, 23))
        self.UpdateButton.setObjectName("UpdateButton")
        self.OpenInGooglMaps = QtWidgets.QPushButton(Form)
        self.OpenInGooglMaps.setGeometry(QtCore.QRect(500, 190, 171, 23))
        self.OpenInGooglMaps.setObjectName("OpenInGooglMaps")
        self.coords_text_label = QtWidgets.QLabel(Form)
        self.coords_text_label.setGeometry(QtCore.QRect(510, 40, 47, 31))
        self.coords_text_label.setObjectName("coords_text_label")
        self.latitude_label = QtWidgets.QLabel(Form)
        self.latitude_label.setGeometry(QtCore.QRect(590, 30, 91, 31))
        self.latitude_label.setObjectName("latitude_label")
        self.longitude_label = QtWidgets.QLabel(Form)
        self.longitude_label.setGeometry(QtCore.QRect(590, 60, 91, 31))
        self.longitude_label.setObjectName("longitude_label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(120, 20, 171, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        icon = QtGui.QIcon.fromTheme("Dark")
        self.comboBox.addItem(icon, "")
        self.Station_chooser_label = QtWidgets.QLabel(Form)
        self.Station_chooser_label.setGeometry(QtCore.QRect(16, 20, 91, 21))
        self.Station_chooser_label.setObjectName("Station_chooser_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.UpdateButton.setText(_translate("Form", "Update coordinates"))
        self.OpenInGooglMaps.setText(_translate("Form", "Open Map on browser"))
        self.coords_text_label.setText(_translate("Form", "Coords:"))
        self.latitude_label.setText(_translate("Form", "None"))
        self.longitude_label.setText(_translate("Form", "None"))
        self.comboBox.setItemText(0, _translate("Form", "International Space Station"))
        self.comboBox.setItemText(1, _translate("Form", "Something Else"))
        self.Station_chooser_label.setText(_translate("Form", "Choose Object"))
