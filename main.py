from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan     #KÜTÜPHANELERİ VE MODÜLLERİ DAHİL EDİYORUZ...
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd
a={
    "Beyaz Yaka":3,
    "Mavi Yaka":5,
    "yönetici":9,

}
b={
    "Beyaz Yaka":3,
    "Mavi Yaka":6,
    "yönetici":1,

}
c={
    "Beyaz Yaka":8,
    "Mavi Yaka":3,
    "yönetici":1,

}


#Nesneleri oluşturma
insan1=Insan("ahmet","akdemir",20,"Erkek","Türk",123456789)
insan2=Insan("ilhan","mansız",20,"Erkek","Türk",987654321)


calisan1=Calisan("Murat","Boz",43,"erkek","Türk",123456789,"diğer",3,12000,a)
calisan2=Calisan("Elon","Musk",32,"Erkek","Güney Amerike",123456789,"Teknoloji",8,22000,a)
calisan3=Calisan("scarlett","johansson",38,"kız","ABD",123456789,"inşaat",8,23000,a)

maviYaka1=MaviYaka("mahsun","Kır",42,"Kız","Türk",987654321,"teknoloji",4,14000,0.2,b)
maviYaka2=MaviYaka("mesut","yılmaz",53,"Erkek","Türk",123456789,"diğer",4,13000,0.5,b)
maviYaka3=MaviYaka("lionel","messi",53,"Erkek","arjantin",123456789,"diğer",4,11000,0.5,b)

beyazYaka1=BeyazYaka("mustafa","sarıgül",55,"erkek","türk",123456789,"diğer",2,14500,500,c)
beyazYaka2=BeyazYaka("tony","stark",55,"erkek","ABD",123456789,"muhasebe",5,13000,1500,c)
beyazYaka3=BeyazYaka("beyza","akdemir",37,"kız","türk",9876543254,"muhasebe",4,12000,2000,c)
#Sözlük oluşturma ve gerekli bilgileri girme
veri={
    "NESNELER":["İnsan1","İnsan2","Çalışan1","Çalışan2","Çalışan3","Mavi yaka1","Mavi yaka2","Mavi yaka3","Beyaz yaka1","Beyaz yaka2","Beyaz yaka3"],
    "T.C":[insan1.get_tc_no(),insan2.get_tc_no(),calisan1.get_tc_no(),calisan2.get_tc_no(),calisan3.get_tc_no(),maviYaka1.get_tc_no(),maviYaka2.get_tc_no(),maviYaka3.get_tc_no(),beyazYaka1.get_tc_no(),beyazYaka2.get_tc_no(),beyazYaka3.get_tc_no()],
    "İSİM":[insan1.get_ad(),insan2.get_ad(),calisan1.get_ad(),calisan2.get_ad(),calisan3.get_ad(),maviYaka1.get_ad(),maviYaka2.get_ad(),maviYaka3.get_ad(),beyazYaka1.get_ad(),beyazYaka2.get_ad(),beyazYaka3.get_ad()],
    "SOYİSİM":[insan1.get_soyad(),insan2.get_soyad(),calisan1.get_soyad(),calisan2.get_soyad(),calisan3.get_soyad(),maviYaka1.get_soyad(),maviYaka2.get_soyad(),maviYaka3.get_soyad(),beyazYaka1.get_soyad(),beyazYaka2.get_soyad(),beyazYaka3.get_soyad()],
    "YAS":[insan1.get_yaş(),insan2.get_yaş(),calisan1.get_yaş(),calisan2.get_yaş(),calisan3.get_yaş(),maviYaka1.get_yaş(),maviYaka2.get_yaş(),maviYaka3.get_yaş(),beyazYaka1.get_yaş(),beyazYaka2.get_yaş(),beyazYaka3.get_yaş()],
    "CİNSİYET":[insan1.get_cinsiyet(),insan2.get_cinsiyet(),calisan1.get_cinsiyet(),calisan2.get_cinsiyet(),calisan3.get_cinsiyet(),maviYaka1.get_cinsiyet(),maviYaka2.get_cinsiyet(),maviYaka3.get_cinsiyet(),beyazYaka1.get_cinsiyet(),beyazYaka2.get_cinsiyet(),beyazYaka3.get_cinsiyet()],
    "UYRUK":[insan1.get_uyruk(),insan2.get_uyruk(),calisan1.get_uyruk(),calisan2.get_uyruk(),calisan3.get_uyruk(),maviYaka1.get_uyruk(),maviYaka2.get_uyruk(),maviYaka3.get_uyruk(),beyazYaka1.get_uyruk(),beyazYaka2.get_uyruk(),beyazYaka3.get_uyruk()],
    "SEKTÖR":[0,0,calisan1.get_sektor(),calisan2.get_sektor(),calisan3.get_sektor(),maviYaka1.get_sektor(),maviYaka2.get_sektor(),maviYaka3.get_sektor(),beyazYaka1.get_sektor(),beyazYaka2.get_sektor(),beyazYaka3.get_sektor()],
    "MAAŞ": [0,0,calisan1.get_maaş(),calisan2.get_maaş(),calisan3.get_maaş(),maviYaka1.get_maaş(),maviYaka2.get_maaş(),maviYaka3.get_maaş(),beyazYaka1.get_maaş(),beyazYaka2.get_maaş(),beyazYaka3.get_maaş()],
    "TECRÜBE":[0,0,calisan1.get_tecrübe(),calisan2.get_tecrübe(),calisan3.get_tecrübe(),maviYaka1.get_tecrübe(),maviYaka2.get_tecrübe(),maviYaka3.get_tecrübe(),beyazYaka1.get_tecrübe(),beyazYaka2.get_tecrübe(),beyazYaka3.get_tecrübe()],
    "YENİ MAAŞ":[0,0,calisan1.zam_hakkı(),calisan2.zam_hakkı(),calisan3.zam_hakkı(),maviYaka1.zam_hakkı(),maviYaka2.zam_hakkı(),maviYaka3.zam_hakkı(),beyazYaka1.zam_hakkı(),beyazYaka2.zam_hakkı(),beyazYaka3.zam_hakkı()],
    "Statü":[0,0,calisan1.statü_bul(),calisan2.statü_bul(),calisan3.statü_bul(),maviYaka1.statü_bul(),maviYaka2.statü_bul(),maviYaka3.statü_bul(),beyazYaka1.statü_bul(),beyazYaka2.statü_bul(),beyazYaka3.statü_bul()]

}
df=pd.DataFrame(veri,[1,2,3,4,5,6,7,8,9,10,11])

print(df)
print("**************************************************")
onbes_ustu_maas=df[df["MAAŞ"]>15000]
print("Maaşı 15000 liranın üzerinde olan kişi sayısı:",len(onbes_ustu_maas),"\n")

print("**************************************************")

kucuk_df=df.sort_values("YENİ MAAŞ")
print("Yeni Maaşa göre sıralama:\n",kucuk_df)


bul=(df["Statü"]=='Beyaz Yaka') & (df['TECRÜBE']>3)
beyaz_yakalar= df[bul]
print(beyaz_yakalar)

print("**************************************************")

seçili_liste = df[(df.index >= 2) & (df.index <= 5) & (df["YENİ MAAŞ"] > 10000)][["T.C", "YENİ MAAŞ"]]
print(seçili_liste)

print("**************************************************")


yeni_df=df[["İSİM","SOYİSİM","SEKTÖR","YENİ MAAŞ"]]
print(yeni_df)


