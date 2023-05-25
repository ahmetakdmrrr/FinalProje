from Insan import Insan
class Issiz(Insan):
     def __int__(self,ad,soyad,tecrübe):
        self.__ad=ad
        self.__soyad=soyad
        self.__tecrübe=tecrübe
        self.__statü=self.statü_bul()
    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
        self.__statu = self.statu_bul()
    def statü_bul(self):
        maks_etki=0
        etki=0
        for statü,yıl in self.__tecrübe.items():
            try:
                yıl=int(yıl)
                etki=0
                if statü=="mavi yaka":
                    etki=yıl/5
                elif statü=="beyaz yaka":
                    etki=(yıl)*(35/100)
                elif statü=="yönetici":
                    etki=(yıl)*(45/100)

                if etki>maks_etki:
                    maks_etki=etki
                    karar_statü=statü
            except:
                print("geçersiz bir yıl veya statü tekrar deneyiniz",yıl)
        if karar_statü=="":
            return "bilinmiyor ne olduğu"
        else:
            return f"belirlendi statü iletiliyor...\n{karar_statü}"
    def __str__(self):
        return f"ad={self.__ad}\nsoyad={self.__soyad}\nstatünüz={self.statü_bul()}\n"

        
