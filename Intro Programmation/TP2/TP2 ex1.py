a = float(input("Longueur a: "))
b = float(input("Longueur b: "))
c = float(input("Longueur c: "))

if (a < (b + c)) or (b < (a + c)) or (c < a + b):
    print("Les longueurs saisies ne vérifient pas l'inégalité triangulaire")
else:
    print("Nickel")
