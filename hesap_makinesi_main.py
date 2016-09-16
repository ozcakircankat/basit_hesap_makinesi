from hesap_makinesi import Ui_Form
from PyQt5.QtWidgets import *


__author__ = "Cankat Özçakır"
__copyright__ = "Copyright 2016, C.Özçakır"
__version__ = "v1.00"



class Arayuz(QWidget,Ui_Form):
    def __init__(self):
        super(Arayuz, self).__init__()
        self.setupUi(self)
        self.hesapla.clicked.connect(self.islem_kontrol)


    def islem_kontrol(self):

        if self.islem_Sec.currentText() == "Toplama +":

            if (self.veri_ilk.text() and self.veri_ikinci.text()).isnumeric():

                self.toplama = int(self.veri_ilk.text()) + int(self.veri_ikinci.text())
                self.sonuc.setText("Sonuç : {}".format(self.toplama))
                self.veri_ilk.clear()
                self.veri_ikinci.clear()

            else:
                self.sonuc.setText("Geçerli değer giriniz!")

#---------------------------------------------------------------

        if self.islem_Sec.currentText() == "Çıkarma -":

            if (self.veri_ilk.text() and self.veri_ikinci.text()).isnumeric():

                self.cikarma = int(self.veri_ilk.text()) - int(self.veri_ikinci.text())
                self.sonuc.setText("Sonuç : {}".format(self.cikarma))
                self.veri_ilk.clear()
                self.veri_ikinci.clear()

            else:
                self.sonuc.setText("Geçerli değer giriniz!")

#---------------------------------------------------------------

        if self.islem_Sec.currentText() == "Çarpma x":

            if (self.veri_ilk.text() and self.veri_ikinci.text()).isnumeric():

                self.carpma = int(self.veri_ilk.text()) * int(self.veri_ikinci.text())
                self.sonuc.setText("Sonuç : {}".format(self.carpma))
                self.veri_ilk.clear()
                self.veri_ikinci.clear()

            else:
                self.sonuc.setText("Geçerli değer giriniz!")

#---------------------------------------------------------------

        if self.islem_Sec.currentText() == "Bölme /":

            if (self.veri_ilk.text() and self.veri_ikinci.text()).isnumeric():

                self.bolme = int(self.veri_ilk.text()) // int(self.veri_ikinci.text())
                self.sonuc.setText("Sonuç : {}".format(self.bolme))
                self.veri_ilk.clear()
                self.veri_ikinci.clear()

            else:
                self.sonuc.setText("Geçerli değer giriniz!")

# ---------------------------------------------------------------

        if self.islem_Sec.currentText() == "Mod %":

            if (self.veri_ilk.text() and self.veri_ikinci.text()).isnumeric():

                self.mod = int(self.veri_ilk.text()) % int(self.veri_ikinci.text())
                self.sonuc.setText("Sonuç : {}".format(self.mod))
                self.veri_ilk.clear()
                self.veri_ikinci.clear()

            else:
                self.sonuc.setText("Geçerli değer giriniz!")

#---------------------------------------------------------------

        if self.islem_Sec.currentText() == "Üs Alma **":

            if (self.veri_ilk.text() and self.veri_ikinci.text()).isnumeric():

                self.us = int(self.veri_ilk.text()) ** int(self.veri_ikinci.text())
                self.sonuc.setText("Sonuç : {}".format(self.us))
                self.veri_ilk.clear()
                self.veri_ikinci.clear()

            else:
                self.sonuc.setText("Geçerli değer giriniz!")


app = QApplication([])

pencere = Arayuz()
pencere.show()

app.exec_()