osoba = ["Sofija", 25, "plava", False]

for x in range(len(osoba)):
    print(osoba[x])
        # ili ovako....
for osobina in osoba:
    print(osobina)
print("-----------------------------------------------------")

voce_i_povrce =["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]

for stavke in voce_i_povrce:
    print(stavke)
    # ili ovako-----

for i in range(len(voce_i_povrce)):
    print("brojevi:", i, voce_i_povrce[i])

    # moze i ovako

for index, vrednost in enumerate(voce_i_povrce):
    print("Index:", index, "Stavka: ", vrednost)

print("-----------------------------------------------------")

automobili = ["Citroen", "BMW", "Opel","Kia", "Yugo", "Opel", "Opel"]

'''for i in range(len(automobili)):
    print("Pozicija:", i, "Auto:", automobili[i])
    # ILI OVAKO---------

for pozicija, auto in enumerate(automobili):
    if pozicija == 2:
        print("kupujem")
        break
    print("Pozicija:", pozicija, "Auto:", auto)
    #i OVAKO

for pozicija, auto in enumerate(automobili):
    if auto == "Opel":
        print(pozicija, auto)
    #print("Pozicija:", pozicija, "Auto:", auto)'''

for pozicija, auto in enumerate(automobili):
    if len(auto) >= 4:
        print(auto)
    
automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
automobili[3] = "Kia Rio"
print(automobili)
                # BRISANJE IZ LISTE SEKVENCE
del automobili[3]
automobili.remove("Opel")
automobili.pop(2)
print(automobili)

automobili[0]
broj_opela = 0
for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("evo ga Opel")
        broj_opela += 1

print("imam ", broj_opela , "na placu")

            # BRISANJE CELE LISTE

'''automobili.clear()
print(automobili)

prazan_plac = []
prazan_plac.append("Mercedes", "BMW", " Audi")'''


#automobili = ["Citroen", "BMW", "Opel","Kia", "Yugo","Peugeot", "Audi"]
#
#automobili_akcija = []
#
#for i in range(len(automobili)):
#    if i == 1 or i == 2 or i == 3:
#        automobili_akcija.append(automobili[i])
#print(automobili_akcija)
#
#automobili_akcija = automobili[1:4:2]
#print(automobili_akcija)


brojevi = [1, 10, 12, 7, 3, 4, 2, 5]
parni = []
neparni = []

'''for broj in brojevi:
    if broj % 2:
        parni.append(broj)
    else:
        neparni.append(broj)
print(parni, neparni)'''

# ILI OVAKO

for broj in brojevi:
    parni.append(broj) if broj % 2 == 0 else neparni.append(broj)

print(parni, neparni)