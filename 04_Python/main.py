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
if True:  #if'den sonra :'ya kadar olan kısım 
    print("Merhaba")
















