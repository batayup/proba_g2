pozicija_automobila = 0
pozicija_cilja = 10

for pozicija_automobila in range(pozicija_cilja):
    print(pozicija_automobila)


print("-------drugi primer------------")

for ime in ["marko", "milos", "marija", "ana", "sofija"]:
    print("Hello", ime)

print("-----------sledeci primer-----")

for broj in [1, 2, 3, 4, 5]:
    print("ovo je broj:", broj)

#  1. br u zagradi = od tog broj_____ 2. br: do kod broja
#  3. br. za koliko se uvecava
for broj in range(1, 21, 2):  
    print("stampanje broja: ", broj)

for broj in range(100, 0, -5):
    print(broj)

print("---------------sledeci---------------")
# Vezba_1
pocetna_godina = 2010
zavrsna_godina = 2021

for godina in range(pocetna_godina, zavrsna_godina):
    print("Allowed years:", godina)


'''for zvezda in range(90):
    print("*", end="")'''

print("--------------nova vezba------------")

# Vezba_2
#print("*********************************")
#print("1\t2\t3\t")
#zeljeni_br = int(input("Unesite broj: "))
#
#for broj in range(1, zeljeni_br + 1):
#    print(broj * 1, end="\t")
#    print(broj * 2, end="\t")
#    print(broj * 3, end="\n")

      # Petlja u Petlji
#for x in range(5):       # x = 0
#    for y in range(3):   # y = 0, 1, 2, 
#        print("ovo je x:", x, "ovo je y:", y)

'''
* * * * * * *
* * * * * * * 
* * * * * * *         
* * * * * * *
* * * * * * *
'''
#for zvezdica in range(6):
#    print("*", end=" ")


'''for x in range(8):
    for y in range(8):
        if x == y:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()'''

# DRUGI PRIMER OVE VEZBE:

'''for x in range(6):
    for y in range(6):
        print("*" if x == y else "#", end=" ")
    print()'''

#        Vezba 3

'''for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()'''







    
