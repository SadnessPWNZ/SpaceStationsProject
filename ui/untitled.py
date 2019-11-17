# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\princ\Desktop\DEV\SchoolProject\ui\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 529)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Form.setFont(font)
        Form.setMouseTracking(False)
        self.UpdateButton = QtWidgets.QPushButton(Form)
        self.UpdateButton.setGeometry(QtCore.QRect(350, 410, 171, 23))
        icon = QtGui.QIcon.fromTheme("Dark")
        self.UpdateButton.setIcon(icon)
        self.UpdateButton.setAutoDefault(False)
        self.UpdateButton.setDefault(False)
        self.UpdateButton.setFlat(False)
        self.UpdateButton.setObjectName("UpdateButton")
        self.OpenInGooglMaps = QtWidgets.QPushButton(Form)
        self.OpenInGooglMaps.setGeometry(QtCore.QRect(350, 440, 171, 23))
        self.OpenInGooglMaps.setObjectName("OpenInGooglMaps")
        self.coords_text_label = QtWidgets.QLabel(Form)
        self.coords_text_label.setGeometry(QtCore.QRect(20, 70, 47, 31))
        self.coords_text_label.setObjectName("coords_text_label")
        self.latitude_label = QtWidgets.QLabel(Form)
        self.latitude_label.setGeometry(QtCore.QRect(100, 60, 91, 31))
        self.latitude_label.setObjectName("latitude_label")
        self.longitude_label = QtWidgets.QLabel(Form)
        self.longitude_label.setGeometry(QtCore.QRect(100, 90, 91, 31))
        self.longitude_label.setObjectName("longitude_label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(120, 20, 171, 21))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        icon = QtGui.QIcon.fromTheme("Dark")
        self.comboBox.addItem(icon, "")
        self.Station_chooser_label = QtWidgets.QLabel(Form)
        self.Station_chooser_label.setGeometry(QtCore.QRect(16, 20, 91, 21))
        self.Station_chooser_label.setObjectName("Station_chooser_label")
        self.VisualPasses = QtWidgets.QPushButton(Form)
        self.VisualPasses.setGeometry(QtCore.QRect(350, 470, 171, 23))
        self.VisualPasses.setObjectName("VisualPasses")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(560, 60, 256, 192))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.UpdateButton.setWhatsThis(_translate("Form", "<html><head/><body><p>Update station coordinates</p><p><br/></p></body></html>"))
        self.UpdateButton.setText(_translate("Form", "Update coordinates"))
        self.OpenInGooglMaps.setWhatsThis(_translate("Form", "<html><head/><body><p>Open current map location of station</p><p><br/></p></body></html>"))
        self.OpenInGooglMaps.setText(_translate("Form", "Open Map on browser"))
        self.coords_text_label.setText(_translate("Form", "Coords:"))
        self.latitude_label.setText(_translate("Form", "None"))
        self.longitude_label.setText(_translate("Form", "None"))
        self.comboBox.setItemText(0, _translate("Form", "International Space Station"))
        self.comboBox.setItemText(1, _translate("Form", "Something Else"))
        self.Station_chooser_label.setText(_translate("Form", "Choose Object"))
        self.VisualPasses.setWhatsThis(_translate("Form", "<html><head/><body><p>Open current map location of station</p><p><br/></p></body></html>"))
        self.VisualPasses.setText(_translate("Form", "Visual Passes"))
