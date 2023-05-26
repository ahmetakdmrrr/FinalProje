from abc import ABC,abstractmethod

class Calisan(ABC,Insan):
    def __int__(self,ad,soyad,maaş,tecrübe,sektor):
        self.__sektor=self.dogru_sektor(sektor)
        self.__ad=ad
        self.__soyad=soyad
        self.__maaş=maaş
        self.__tecrübe=tecrübe
        self.__zam_hakkı=self.zam_hakkı()
    def dogru_sektor(self,sektor):
        sektor=sektor.lower()
        if sektor=="teknoloji" or sektor=="muhasebe" or sektor=="inşaat" or sektor=="diğer":
            return sektor
        else:
            print("geçersiz bir sektor girdiniz o yüzden diğer seçeneği seçildi.\n")
            return "diğer"
