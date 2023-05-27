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
    def zam_hakkı(self):
        b= ""
        yıpranma_payı=0.5
        try:
            maaş = int(self.__maaş)
            if self.__tecrübe >= 0:
                if self.__tecrübe < 24:
                    b = "maaşınıza zam yapılıyor...\n"
                    zam_oranı=yıpranma_payı*10
                    self.__maaş=self.__maaş+(self.__maaş*(zam_oranı/100))
                elif self.__tecrübe < 48 and self.__tecrübe >= 24:
                    if self.__maaş < 15000:
                        b = "maaşınıza zam yapılıyor...\n"
                        zam_oranı= ((self.__maaş%self.__tecrübe)/2) + (yıpranma_payı*10)
                        self.__maaş=self.__maaş+(self.__maaş*(zam_oranı/100))
                elif self.__tecrübe > 48 and self.__maaş < 25000:
                    b = "maaşınıza zam yapılıyor...\n"
                    zam_oranı = ((self.__maaş%self.__tecrübe)/3) + (yıpranma_payı*10)
                    self.__maaş = self.__maaş + (self.__maaş*(zam_oranı/100))
            else:
                b = "tecrübe girişinizde hata bulunmaktadır..."
        except:
            return "girdilerinizde hata buluhmaktadır tekrar deneyiniz"

        return f"{b}\n{self.__maaş}"
    def __str__(self):
        return f"isim={self.__ad}\nsoyisim={self.__soyad}\ntecrübe={self.__tecrübe} ay\nyeni maaş={self.zam_hakkı()}"

