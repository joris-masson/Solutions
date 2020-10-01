#1----------------------------------------------------------
print("1.")
ch = input("Veuillez marquer quelque chose: ")
car1 = input("Caractère 1: ")
car2 = input("Caractère 2: ")

nbCar1 = 0
nbCar2 = 0

for i in ch:
    if str(i) == car1:
        nbCar1 += 1
    elif str(i) == car2:
        nbCar2 += 1
print("Il y a, ", nbCar1, car1, "et " , nbCar2, car2, "dans ce que vous avez entré \n")

#2----------------------------------------------------------
print("2.")
ch = input("Veuillez marquer quelque chose: ")
car1 = input("Caractère 1: ")
car2 = input("Caractère 2: ")

phrase = ""

for i in ch:
    if str(i) == car1:
        phrase += car2
    elif str(i) == car2:
        phrase += car1
    else:
        phrase += i
print(phrase)
