""" 
#str "Ayşe" , int 5, float 5.5, bool True/False

#veriable=değişken
yil = 2024

#type() fonksiyonu, verinin türünü döndürür
print(type(yil))

#input() fonksiyonu, kullanicidan bir değer alir
#type convertion, verinin türünü değiştirir
dogum_yili = int((input("Doğum yilinizi giriniz: ")))
print(yil - dogum_yili) 
"""



"""
#list'de köşeli parantezlerin[] içine virgülle ayrılmış değişkenler listesi tanımlayabiliyoruz
isim_listesi = ["Ali", "Ali", 2005, "Istanbul", 70.5, True]
print(type(isim_listesi))
print(type(isim_listesi[0])) #listenin elemanının type'na bakılır, 0 baştan ilk eleman, -1 sondan ilk eleman

#list'ler siralanabilir, değiştirilebilir, yineleniblir(tekrar edilebilir)
isim_listesi[1] = "Veli"
print((isim_listesi[1]))

#listenin kendine ait metodları vardır. Listenin adının sonuna nokta koyarsak metodlar önerilir.
isim_listesi.append(1) #parantez içindekini listenin sonuna ekler
isim_listesi.insert(0, "Ayşe") #belirtilen pozisyona ekler
isim_listesi.remove("Ali") #belirtilen değeri ilk bulduğu yerde siler
isim_listesi.reverse() #listedeki sıralamayı tersine çevirir
#isim_listesi.sort() #str sözlük sırasına göre sıralar, int küçükten büyüğe sıralar, farklı değerleri bilgisayarın atadığı değere göre sıralar
isim_listesi.clear #listedekileri siler

print(isim_listesi)

#OPERATÖRLER
#aritmetik operatötler +, -, /, *, **, //, %
sonuc = 3 ** 2 # ** sayının üssünü alır. 
sonuc = 3 // 4 # // sonuç ondalık sayı ise tam sayı olarak alır
sonuc = 7 % 4 # sayının modunu alır
print(sonuc)

#assignment operatörler. en sık kullanılanı eşittirdir (=)   =, +=, -=, *=, /=, %=, **=, //=
sonuc = 0 #eşittirin karşisina yazdiğimiz şeyi sonucun içine yerleştiriyor
sonuc += 5 #sonucu 5le toplayıp tekrar sonucun içine yazdırıyor
print(sonuc)

#comparison(kıyaslama) operatörler ==(eşit mi), !=(eşit değil mi), >, <, <=, >=
sonuc = (0 == 0) #2 eşdeşin karşı taraflarını birbiriyle kıyaslar, birbirine eşit ve denkse True döndürür sonucun içine True yazdırır. 
sonuc = (0 == "0") #2 taraf kıyaslanabilir olmalı yoksa otomatikmen False döndürür.
print(sonuc)

#logical(mantıksal) oparatörler and, or, not
sonuc = (0 >= 1) and (1 < 2) or (3 == 3) #blokları tek tek çözüp sonra diğer üst bloğu çözer
#        False   and  True   or   True   #soldan başlayarak kıyaslamaya devam eder. And'lerken 2side True ise True, herhangi birisi False ise False döner
                                         #Or'da ise herhangi birisi True ise True döner.                                          
print(sonuc)

#IF ve FOR döngüleri
if True:  #if'den sonra :'ya kadar olan kısım if'in koşulu olur. Eğer koşul doğru ise True ise if'in :'dan itibaren boşlukla başlayan tüm satırlar
    print("Merhaba")     #if koşulunun kodlarıdır, if geçerliyse çalışır. İf'le aynı hizada yazılan kod ise if'den bağımsız çalışır. 

print("The End")

if (2 > 1) and (3 != 2):
    print("Merhaba")
    print("Merhaba")

print("The End") 

if 6 not in [1, 2, 3, 4, 5]:
    print("Listede yok")
elif 6 not in [6, 7, 8, 9,]:
    print("Naber")
else:
    print("Listede var")

#Alıştırma
kullanici_girisi = input("Mesafeyi giriniz: ") #'1000 K', '1000 M'
girdi_listesi = kullanici_girisi.split( )
mesafe = int(girdi_listesi[0])
birim = girdi_listesi[1].upper()

KM2MILE = 0.621371192

KM_birimleri = ["KM", "K", "KILOMETRE"]
Mile_birimleri =  ["MILE", "M", "MIL"]

if birim in KM_birimleri:
    print("Mesafe mile cinsinden: " + str(mesafe * KM2MILE))
elif birim in Mile_birimleri:
    print("Mesafe km cinsinden: " + str(mesafe / KM2MILE))
else:
    print("Hatalı birim girdiniz!")
"""


