from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, ad, soyad, yaş, cinsiyet, uyruk, tc_no, sektor, tecrube, maas, a,statü):
        self.__statü=statü
        self.__yaş = yaş
        self.__uyruk = uyruk
        self.__tc_no = tc_no
        self.__sektor = sektor
        self.__cinsiyet = cinsiyet
        self.__ad = ad
        self.__soyad = soyad
        self.__maaş = maas
        self.__tecrübe = tecrube
        self.__zam_hakki = self.zam_hakkı()

    def get_maaş(self):
        return self.__maaş
    def get_sektor(self):
        return self.__sektor
    def get_cinsiyet(self):
        return self.__cinsiyet

    def get_ad(self):
        return self.__ad

    def get_tc_no(self):
        return self.__tc_no
    def dogru_sektor(self,sektor):
        sektor=sektor.lower()
        if sektor=="teknoloji" or sektor=="muhasebe" or sektor=="inşaat" or sektor=="diğer":
            return sektor
        else:
            print("geçersiz bir sektor girdiniz o yüzden diğer seçeneği seçildi.\n")
            return "diğer"
    def get_soyad(self):
        return self.__soyad
    def get_yaş(self):
        return self.__yaş
    def get_uyruk(self):
        return self.__uyruk

    def get_tecrübe(self):
        return self.__tecrübe
    def statü_bul(self):
        maks_etki=0
        etki=0
        for statü,yıl in self.__statü.items():
            try:
                yıl=int(yıl)
                etki=0
                if statü=="Mavi Yaka":
                    etki=yıl/5
                elif statü=="Beyaz Yaka":
                    etki=(yıl)*(35/100)
                elif statü=="yönetici":
                    etki=(yıl)*(45/100)

                if etki>maks_etki:
                    maks_etki=etki
                    karar_statü=statü
            except:
                return "geçersiz bir yıl veya statü tekrar deneyiniz"
        if karar_statü=="":
            return "bilinmiyor ne olduğu"
        else:

            return karar_statü


    def set_maaş(self, maaş):
        self.__maaş = maaş


    def set_tecrübe(self, tecrübe):
        self.__tecrübe = tecrübe


    def zam_hakkı(self):
        a=""
        self.__teşvik_primi=2500
        try:
            maaş = int(self.__maaş)
            if self.__tecrübe >= 0:
                if self.__tecrübe < 24:
                    a = "maaşınıza zam yapılıyor...\n"
                    zam_öneri=self.__teşvik_primi
                    self.__maaş=self.__maaş + zam_öneri
                elif self.__tecrübe < 48 and self.__tecrübe >= 24:
                    if self.__maaş < 15000:
                        a = "maaşınıza zam yapılıyor...\n"
                        zam_miktarı = ((self.__maaş%self.__tecrübe)*5) + self.__teşvik_primi
                        self.__maaş = self.__maaş  + zam_miktarı
                elif self.__tecrübe > 48 and self.__maaş < 25000:
                    a = "maaşınıza zam yapılıyor...\n"
                    zam_miktarı = ((self.__maaş%self.__tecrübe)*4) + self.__teşvik_primi
                    self.__maaş = self.__maaş  + zam_miktarı
            else:
                a = "tecrübe girişinizde hata bulunmaktadır..."
        except:
            return "girdilerinizde hata buluhmaktadır tekrar deneyiniz"
        return self.__maaş

    def __str__(self):
        return f"isim={self.__ad}\nsoyisim={self.__soyad}\ntecrübe={self.__tecrübe} ay\nyeni maaş={self.zam_hakkı()}"
