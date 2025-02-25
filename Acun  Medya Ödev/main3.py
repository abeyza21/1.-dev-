# sınıflar -> claslar 
# modules 
# paket yönetisi
# self => this 
class Human :
    name=" Ayşe "
    #built-in
    def _init_(self):
        print("Bir human instance si üretildi")
    def talk (self,sentence):
        name=" Sara "
        print(f"{self.name} :{sentence}  ") # { name} dersek sarayı görür {self.name} dersek  ayşeyi görür.
    def walk(self):
        print(F"{self.name}is walking ")

#instance => örnek 
human1=Human()
human1.name=" Hanife "
human1.talk(" Merhaba ")
human1.walk()
print(human1)

human2= Human("Ayşe")
human2.talk("selam")
human2.walk() 
print(human2)

