from abc import ABC,abstractmethod

class Insan(ABC):
    def __int__(self,tc_no,ad,soyad,yaş,cinsiyet,uyruk):
        self.__tc_no=tc_no
        self.__ad=ad
        self.__soyad=soyad
        self.__yaş=yaş
        self.__cinsiyet=cinsiyet
        self.__uyruk=uyruk
    def get_tc_no(self):
        return self.__tc_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_yaş(self):
        return self.__yaş

    def get_cinsiyet(self):
        return self.__cinsiyet

    def get_uyruk(self):
        return self.__uyruk

    def set_tc_no(self,tc_no):
        self.__tc_no=tc_no

    def set_ad(self,ad):
        self.__ad=ad

    def set_soyad(self,soyad):
        self.__soyad=soyad

    def set_yaş(self,yaş):
        self.__yaş=yaş
        
    def set_cinsiyet(self,cinsiyet):
        self.__cinsiyet=cinsiyet

    def set_uyruk(self,uyruk):
        self.__uyruk=uyruk
    def __str__(self):
        return f"tc kimlik numarası={self.__tc_no}\nadı={self.__ad}\nsoyadı={self.__soyad}\nyaşı={self.__yaş}\ncinsiyeti={self.__cinsiyet}\nuyruk bilgisi={self.__uyruk}"

