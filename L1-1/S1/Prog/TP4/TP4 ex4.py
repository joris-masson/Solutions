#1---------------------------------------------------
print("1.")
n = int(input("Table: "))
p =int(input("Jusqu'à: "))

res = 0

for i in range(1, p+1):
    res = n * i
    print(n, "x", i, "=", res)
print("\n")
#2---------------------------------------------------
print("2.")
n = int(input("Table: "))
p =int(input("Jusqu'à: "))

res = 0

for i in range(1, p+1):
    res = n * i
    print((i*" "), n, "x", i, "=", res)
print("\n")
#3---------------------------------------------------
print("3.")
n = int(input("Table: "))
p =int(input("Jusqu'à: "))

res = 0

for i in range(1, p+1):
    res = n * i
    if i %2 == 0:
        print("   ", n, "x", i, "=", res)
    else:
        print(n, "x", i, "=", res,"   ")
print("\n")
#4---------------------------------------------------
print("4.")
n = int(input("Table: "))
p =int(input("Jusqu'à: "))

res = 0 #Variable contenant le résultat d'une mult

espaces = 0 #initialise un compteur d'espace

for i in range(1, p+1):
    res = n * i #fait le calcul de table de mult
    if i <= p / 2: #si on a pas dépassé la moité de p
        espaces += 1 #augmente le nb d'espace de 1
    else:
        espaces -= 1 #diminue le nb d'espace de 1
    print((espaces*" "), n, "x", i, "=", res) #affiche espaces " "(donc un espace), et affiche le résultat de la mult
    
print("\n")
#5---------------------------------------------------
print("5.")
n = int(input("Table: "))
p =int(input("Jusqu'à: "))

res = 0
    
print("\n")
input()
