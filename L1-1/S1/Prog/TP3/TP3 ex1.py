#1----------------------------------------------------------
print("1.")
for i in range(1,11):
    print(i, "Bonjour \n")

#2----------------------------------------------------------
print("2.")
min_ = 1
max_ = 10**4
res = 0

for n in range(min_, max_+1):
    res += 1 / (n**2)
print(res, "\n")

#3----------------------------------------------------------
print("3.")
entier = int(input("Entrez un entier: "))
res = 1

for i in range(1, entier+1):
    res *= i
print(entier, "! =", res, "\n")

#4----------------------------------------------------------
print("4.")
a = int(input("Entier 1: "))
b = int(input("Entier 2: "))
res = 0

if a > b:
    for i in range(b, a+1):
        res += i**3
elif a < b:
    for i in range(a, b+1):
        res += i**3
print(res)
