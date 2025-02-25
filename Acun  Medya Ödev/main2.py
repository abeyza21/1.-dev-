faiz=1.56
vade=36
krediadi="İhtiyaç Kredisi"

print(vade+12)
print(type(faiz))
print(type(vade))
print(type(krediadi))

print(int (vade)+12)
#print(int(krediadi)) bu str integere çevrilemez 
faiz=str(faiz)
print(type(faiz))

vade =input("istegiğiniz vade giriniz ")# kullanıcıdan girdi
print(vade)
print(type(vade))
print(int(vade)+12)
#ya da
vade =int(input("istegiğiniz vade giriniz "))# kullanıcıdan girdi
print(vade)
print(type(vade))
print(vade+12)

#string interpolation 
#seçtiğiniz vade sonuçu ortaya çıkan vade sonucu
print("seçtiğiniz vade sonucu ortaya cıkan vade :"+ str(vade))
print("seçtiğiniz vade sonuçu ortaya çıkan vade sonucu {vadeSayisi}".format(vadeSayisi=vade) )

isim ="Ayşe"# input isminizi girinizde yapıp kullanıcıdan alabiliriz
metin =" Merhaba {name}".format(name=isim)
print(metin)

#f-string
metin=f"Hoşgeldiniz {isim}"
print(metin)

# listeler
# döngüler 
#fonksiyonlar
krediler=["ihtiyaç kredisi","Taşıt kredisi", "konut kredisi"]
print(type(krediler))
print(krediler)
print(krediler[0]) # köşeli parantezdeki sayı listenin kaçıncı elemnını yazdırdığını söylüyor 
print(len(krediler))# listedeki eleman sayısı length
# print(krediler[3]) hata verir çünkü listeler 0 dan yaılmaya başlanır 


dizi=["ihtiyaç kredisi",10,3.5 , True]# hata almayız 
print(dizi)

krediler.append("özel krediler")
print(krediler)

krediler.append("x kredisi")
print(krediler)

# eleman silme 
krediler.pop (0)
print(krediler)

krediler.append("Taşıt kredisi")
print(krediler)

krediler.append("yeni kredi ")
print(krediler)

krediler.remove("Taşıt kredisi")# değer değil indeks bazlı çalışıyor   mesela iki yerde vaar birini siliyor diğerini çalıştırıyor 
print(krediler)

krediler.extend([" y kredisi "," z kredisi"])
print(krediler)

#for 
#i=0 i<10 
for i in range(10):
    print("xx")
    print(i)
print("*****")

for i in range (5,10):
    print (i)
print("******")

for i in range(0,5,10):
    print(i)
print("****")
# for i in range(0.1,0.15):
#     print(i)
krediler=["ihtiyaç kredisi","Taşıt kredisi", "konut kredisi"]
for kredi in krediler:
    print(kredi)
print("*****")

for i in range (len (krediler)):
    print (krediler[i])


while True:
    print("x")
    break
print("y")

i=0
while i<10:
    print("x")
    i+=1
print("y")
print("****")

while True:
    print("x")
    break
print("*****")


i=0
while i< len(krediler):
    if krediler[i] == "Konut kredisi":
        break
    print(krediler[i])
    i+=1
    if krediler[i] == "konut kredisi":
        break

while i< len(krediler):
    i+=1
    print(i)
    print(krediler)
    if krediler[i]== "konut kredisi":
        break

# fonksiyonlar 

print("merhaba ")
print("merhaba ")
print("merhaba ")
print("merhaba ")
print("merhaba ")
print("merhaba ")

fiyat=100
indirim =20
# yeni_fiayt =fiyat - indirim 
# yeni_fiyat2= fiyat - indirim 
# yeni_fiayt3=fiyat - indirim 

#defination  define 
def calculate():
    print(100-20)
def calculatewithparams():
    print()

def sayHello(name):
    print(f"merhaba { name}")
calculate()
calculatewithparams(50,10)
calculatewithparams(100,30)
sayHello("Ayşe ")
sayHello("Sara")
    
def calculateAndReturn ( fiyat,indirim ):
    return fiyat-indirim 

yeni_fiyat=calculateAndReturn(200,50)
print(yeni_fiyat+10)

def calculatePrice(price, discount):
    print(price-discount)

def calculatorPriceAndReturn(price,discount):
    return price - discount

print("****")
fonk1= calculatePrice(100,50)
fonk2=calculateAndReturn(300,100)
print(f"174. satir {fonk1}")
print(f"176.satir:{fonk2+100}")
print("******")






