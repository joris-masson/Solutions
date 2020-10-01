"""
Pas fait la 5 parce que flemme.
"""

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

res = 0

espaces = 0

for i in range(1, p+1):
    res = n * i
    if i <= p / 2:
        espaces += 1
    else:
        espaces -= 1
    print((espaces*" "), n, "x", i, "=", res)
    
print("\n")
#5---------------------------------------------------
print("5.")
n = int(input("Table: "))
p =int(input("Jusqu'à: "))

res = 0
    
print("\n")
