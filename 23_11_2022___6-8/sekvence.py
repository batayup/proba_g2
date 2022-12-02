#           0   ,  1  ,   2  ,   3
osoba = ["Sofija", 20, "plava", True]
print(osoba)

print(osoba[0])
print("godine:", osoba[1])

for x in range(10, 2, -2):
    print(x)

#       012345
kurs = "python"
print(kurs[0])
print(kurs[1])
print(kurs[2])
print(kurs[3])

# len(sekvenca)-------odredjuje koliko sekvenca ima karaktera
#duzina = len(kurs)
#print(duzina)

for x in range(6):  # ili u (len(kurs))
    print("na poziciji: ", x ,kurs[x])

ustanova = "It Academy"

for index in range(len(ustanova)):
    print(ustanova[index])

print("-----------------------------------------------------")

primer = "zadatak1"

for index in range(len(primer)):
    print("svako slovo:", primer[index])

# while primer
duzina_karaktera = len(primer)
index = 0

while index < duzina_karaktera:
    print(primer[index])
    index += 1

print("-----------------------------------------------------")

korisnicko_ime = "admin"
uneto_kor_ime = input("unesite korisnicko ime:")

if korisnicko_ime == uneto_kor_ime:
    print("Dobrodosli")
else:
    print("pogresna lozinka")
    