'''brojevi = [9, 1, 3, 2, 5, 8, 7]

brojevi.sort()    # sortiranje brojeva od najveceg ka najnizem
brojevi.reverse() # sortiranje brojeva sa desna na levo

print(brojevi)'''

            # RUCNO SORTIRANJE

'''brojevi = [9, 1, 3, 2, 5, 8, 7]
while True:
    izvrsena_zamena = False
    for i in range(1, len(brojevi)):
        if brojevi[i] < brojevi[i-1]:
            privremena = brojevi[i]
            brojevi[i] = brojevi[i-1]
            brojevi[i-1] = privremena
            izvrsena_zamena = True
    if izvrsena_zamena == False:
        break

print(brojevi)'''

#proizvodi = ["tel", "tv", "lap-top"]
#cene = [100, 200, 500]
#
#for i in range(0, len(proizvodi)):
#    print(proizvodi[i], ":", cene[i])


'''automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugeot"]

for i in range(len(automobili)):
    if i == 3:
        print("Aleksandra vozi:", automobili[i])'''


            #VISE DIMENZIONALNA SLIKA


#telefoni = ["iphone 11", "samsung s22", "xiaomi x3"]
#laptopovi = ["acer", "macbook", "dell"]
#tableti = ["ipad", "samsung galaxy tab", "xiaomi tab"]

# Proizvodi = [telefoni, laptopovi, tableti]

#print(proizvodi[0][0])   # iphone 11 
#print(proizvodi[1][1])   # macbook


'''proizvodi = [
["iphone 11", "samsung s22", "xiaomi x3"],   #0
["acer", "macbook", "dell"],                 #1
["ipad", "samsung galaxy tab", "xiaomi tab"] #2
            ]

#for kategorija in proizvodi:
#    for stavka in kategorija:
#        print(stavka)

for i in range(len(proizvodi)):
    print(proizvodi[i])
    for j in range(len(proizvodi[i])):
        print(proizvodi[i][j])'''


#hrana = [
#            ["cokolada", "bombone","palacinke"],
#            ["sarma", "musaka", "kiseli kupus"],
#            ["pecena paprika", "ajvar", "sopska"]
#        ]
#
#for kategorija in hrana:
#    for jelo in kategorija:
#        print("naziv:", jelo)


'''ime = "sofija ", "nada", "jovana"
poruka = f"cao {ime[1]} "  #formatiran string
print(poruka)'''


biblioteka = [
            ["neki naslov", "neki autor", 123],
            ["neki naslov1", "neki autor1", 122],
            ["neki naslov2", "neki autor2", 121]
]

while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        naslov = input("unesite naslov:")
        autor = input("Unesite autora:")
        isbn = int(input("Unesite isbn:"))
        biblioteka.append([naslov, autor, isbn])
        print("dodata knjiga")
    
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
                




    