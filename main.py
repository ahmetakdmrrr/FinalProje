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

