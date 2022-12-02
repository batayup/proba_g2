
#for x in range(1, 7):
#    for y in range(5):
#        print("#", end="ABCD")
#    print("novi red")

'''for x in range(10):
    for y in range(10):
        if y > x:
            print("#", end="")
        else:
            print(" ", end="")
    print()'''


auto = 0
cilj = 100
brzina = 5
gorivo = 20

while auto < cilj:
    print("voznja je u toku")
    auto += brzina
    gorivo -= 5
    if gorivo == 0:
        print("nemate goriva")
        break

else:
    print("stigli ste")

