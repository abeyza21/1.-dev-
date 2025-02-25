print("Kodlama")
başlik="Taşit kredisi"
print(başlik)
# string => metinsel ifade 
başlik ="İhtiyaç kredisi"
print(başlik )
# int ,integer=> tam sayı 
vade= 36
ekvade=6
vade2="36"

#float, decimal, double 
aylikodeme=200.50
#bool , boolean => true  veya false
yukselistemi= False 
#matematiksel operatörler 
#+
print(5+5)
print(vade +12)
print( vade + ekvade)
print(36+6)
#-
print (5-5)
print( vade - ekvade )
print(vade-12)
#*
print(5*5)
print(vade*2)
print(vade * ekvade)
print(10*10)
#/
print(5/5)
print(vade/2)
print(vade/ekvade)
print(10/2)

yenivade= vade/2
fiyat= 100
indirimliFiyat=fiyat-20
print(yenivade)
print(indirimliFiyat )
# % => mod operatörü 
print(10%2)
print(vade%5)
print(vade % ekvade)
print(30%10)
# mantıksal operatörler
print(1==1)
print(1==2)
# CTRL K + CTRL C yorum satırı halne getirmek için CTRL Ö de kullanılabiri 
#print(1>2)
#print(3>1)
#print(1>1)
#print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)
 
print(1!=1)
print(1!=2)

# or and 

# or => veya 
print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2 )
print(3>2)
print( True and False)
print(1>2 and 5>2 and 3>2)
print(2>1 or 1>2 and 3>2 )
# karar yapıları 
#if else 
sayi1= 10
sayi2=15
#sayi1 sayi2 den büyükse ekrana sayi 1 daha büyük yazdır 
#condution
#indent

if sayi1> sayi2:
    print("sayi1 sayi2 den daha büyük ")# bir intent içerde olmak zorunda yoksa hatalı olur.
    print("hala if in içindeyim")
print("şuan ifin dişindayim")


if sayi1<sayi2:
    print("sayi1 sayi2 den daha büyük ")# bir intent içerde olmak zorunda yoksa hatalı olur.
    print("hala if in içindeyim")
print("şuan ifin dişindayim")


if sayi1> sayi2:
    print("sayi1 sayi2 den daha büyük ")# bir intent içerde olmak zorunda yoksa hatalı olur.
    print("hala if in içindeyim")
# eğer başka durum varsa 
else:
    print("Sayı 1 sayi 2 den küçüktür ")

sayi1=15
sayi2=15

if sayi1> sayi2:
    print("sayi1 sayi2 den daha büyük ")# bir intent içerde olmak zorunda yoksa hatalı olur.
    print("hala if in içindeyim")
# eğer başka durum varsa 
elif sayi1==sayi2:
     print(" iki sayi eşittir ")
else:
    print("Sayı 1 sayi 2 den küçüktür ")


if sayi1<=sayi2:
    print("Sayi1 sayi2  den küçüktür")
if sayi1==sayi2:# burda farklı bir koşula geçiş yapıyor eğer içi içe şart istiyorsak elif i kullan 
    print("iki sayi eşittir")
else:
    print("sayi1 sayi2 den büyüktür ")
print("burası if bloğunun dışındadır ")


