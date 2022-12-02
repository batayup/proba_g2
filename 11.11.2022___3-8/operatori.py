import random

kurs = "Python Fundamentals"
print(kurs)

a = 10
b = 5
print(a + b)

rez_sabiranja = a + b
rez_oduzimanja = a - b
rez_mnozenja = a * b
rez_deljenja = int(a / b)

print("Sabiranje: ", rez_sabiranja)
print("Oduzimanje: ", rez_oduzimanja)
print("Mnozenje: ", rez_mnozenja)
print("Deljenje: ", rez_deljenja)

print("Celobrojno deljenje: ", 10 // 3)

print("Stepenovanje: ", a ** 2)  # 10 na kvadrat---a * a = 100
print("Stepenovanje: ", a ** 3)  # 10 na treci-----a * a * a = 1000

print("Modulo: ", 10 % 3) #ostatak od celog broja kod deljenja 10/3=1

print(-a) # Unarni operator a = 10___rez -10

godine = 25
godine = 25 + 1 

print(godine)

godine *= 2
print(godine)

godine /= 2   # //= je za ceo broj, bez decimale
print(godine)

a = a + 3  # isto moze i ovako_____a += 3
print(a)

'''broj1 = int(input("Unesite prvi broj: "))

broj2 = int(input("Unesite drugi broj: "))

print("Rezultat: ", broj1 + broj2)'''

'''poluprecnik = float(input("Unesite poluprecnik: "))
pi = 3.14

povrsina = poluprecnik ** 2 * pi
print("Povrsina kruga je: ", povrsina)'''

stara_kg = 80
nova_kg = 99

print(stara_kg > nova_kg)
print(stara_kg < nova_kg)
print(nova_kg == 100)
print(stara_kg != 100)  # znak za razlicitosti

username = "test"
password = "abc123"

#godine = int(input("Unesite godine: "))
#print(godine >= 16)

'''broj = int(input("Unesite broj: "))

# % modulo

provera = broj % 2
print("Paran broj? ", provera == 0)'''

#korisnik = int(input("Unesite broj: "))
#racunar = random.randint(1, 10)

#print("Korisnik: ", korisnik)
#print("Racunar: ", racunar)
#print("Pogodak: ", korisnik == racunar)

'''godine = 13
korisnik = int(input("Broj godina: "))

print("Dozvoljeno: ", godine <= korisnik)'''

provera_imena = True # ime == sacuvano_ime
provera_sifre = False # sifra == sacuvana_sifra

print(provera_imena and provera_sifre)

'''
and...
true true  -> true
true false -> false
false false-> false
or...
true true  -> true
true false -> true
false false-> false
'''
#lepo_vreme = True
#print(not lepo_vreme)

kurs = input("Unesite kurs: ")
generacija = int(input("Unesite generaciju: "))

provera_kurs = kurs == "Python"
provera_generacija = generacija == 2022

#odobreno = kurs == "Python" and generacija == 2022
odobreno = provera_kurs and provera_generacija
print("Dozvoljen pristup: ", odobreno)










