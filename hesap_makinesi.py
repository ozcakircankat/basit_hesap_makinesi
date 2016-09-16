# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hesap_makinesi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 172)
        Form.setMinimumSize(QtCore.QSize(451, 172))
        Form.setMaximumSize(QtCore.QSize(451, 172))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calculator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.veri_ilk = QtWidgets.QLineEdit(Form)
        self.veri_ilk.setGeometry(QtCore.QRect(130, 30, 281, 21))
        self.veri_ilk.setObjectName("veri_ilk")
        self.sayi_ilk = QtWidgets.QLabel(Form)
        self.sayi_ilk.setGeometry(QtCore.QRect(40, 30, 91, 21))
        self.sayi_ilk.setObjectName("sayi_ilk")
        self.sayi_ikinci = QtWidgets.QLabel(Form)
        self.sayi_ikinci.setGeometry(QtCore.QRect(40, 80, 81, 19))
        self.sayi_ikinci.setObjectName("sayi_ikinci")
        self.veri_ikinci = QtWidgets.QLineEdit(Form)
        self.veri_ikinci.setGeometry(QtCore.QRect(130, 80, 281, 21))
        self.veri_ikinci.setObjectName("veri_ikinci")
        self.islem_Sec = QtWidgets.QComboBox(Form)
        self.islem_Sec.setGeometry(QtCore.QRect(320, 120, 111, 31))
        self.islem_Sec.setObjectName("islem_Sec")
        self.islem_Sec.addItems(["Toplama +","Çıkarma -","Çarpma x","Bölme /","Mod %","Üs Alma **"])
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 411, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.hesapla = QtWidgets.QPushButton(Form)
        self.hesapla.setGeometry(QtCore.QRect(20, 120, 112, 31))
        self.hesapla.setObjectName("hesapla")
        self.sonuc = QtWidgets.QLabel(Form)
        self.sonuc.setGeometry(QtCore.QRect(150, 110, 241, 41))
        self.sonuc.setObjectName("sonuc")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(140, 110, 171, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.frame.raise_()
        self.frame_2.raise_()
        self.veri_ilk.raise_()
        self.sayi_ilk.raise_()
        self.sayi_ikinci.raise_()
        self.veri_ikinci.raise_()
        self.islem_Sec.raise_()
        self.hesapla.raise_()
        self.sonuc.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hesap Makinesi"))
        self.sayi_ilk.setText(_translate("Form", "Birinci Sayı:"))
        self.sayi_ikinci.setText(_translate("Form", "İkinci Sayı:"))
        self.hesapla.setText(_translate("Form", "Hesapla"))
        self.sonuc.setText(_translate("Form", "Sonuç :"))