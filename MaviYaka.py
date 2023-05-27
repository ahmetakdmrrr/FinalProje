from Calisan import Calisan
class MaviYaka(Calisan):

    def __init__(self, ad, soyad, maas, tecrube):

        self.__ad = ad
        self.__soyad = soyad
        self.__maaş = maas
        self.__tecrübe = tecrube
        self.__zam_hakki = self.zam_hakkı()

    def get_maaş(self):
        return self.__maaş


    def get_tecrübe(self):
        return self.__tecrübe


    def set_maaş(self, maaş):
        self.__maaş = maaş


    def set_tecrübe(self, tecrübe):
        self.__tecrübe = tecrübe
