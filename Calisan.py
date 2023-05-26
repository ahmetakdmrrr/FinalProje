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
    def get_sektor(self):
        return self.__sektor
    def set_sektor(self,sektor):
        self.__sektor=self.dogru_sektor()

    def get_maaş(self):
        return self.__maaş
    def get_tecrübe(self):
        return self.__tecrübe
    def set_maaş(self,maaş):
        self.__maaş=maaş
    def set_tecrübe(self,tecrübe):
        self.__tecrübe=tecrübe
    def zam_hakkı(self):
        a=""
        try:
            maaş=int(self.__maaş)
            if self.__tecrübe>=0:
                if self.__tecrübe<24:
                    a="maaş zam hakkınız bulunmamaktadır."
                elif self.__tecrübe<48 and self.__tecrübe>24:
                    if self.__maaş<15000:
                        a="maaşınıza zam yapılıyor...\n"
                        zam_miktarı=self.__maaş%self.__tecrübe
                        self.__maaş=self.__maaş+zam_miktarı
                elif self.__tecrübe>48 and self.__maaş<25000:
                    a="maaşınıza zam yapılıyor...\n"
                    zam_miktarı=(self.__maaş%self.__tecrübe)/2
                    self.__maaş=(self.__maaş)+(zam_miktarı)
                else:
                   a="tecrübe girişinizde hata bulunmaktadır..."
        except:
            return "girdilerinizde hata buluhmaktadır tekrar deneyiniz"
        return f"{a}\n{self.__maaş}"
    def __str__(self):
        return f"yeni maaşı={self.zam_hakkı()}\nisim={self.__ad}\nsoyisim={self.__soyad}\ntecrübe={self.__tecrübe}"
    
