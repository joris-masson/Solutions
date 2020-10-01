n = int(input("Donnez un entier: "))

if ((n%3) == 0) and ((n%5) == 0):
    print("n est divisible par 3 et 5")
elif ((n%3 == 0) and ((n%5) != 0)):
    print("n est divisible par 3, mais pas par 5")
elif ((n%3 != 0) and ((n%5) == 0)):
    print("n est divisible par 5, mais pas par 3")
else:
    print("n n'est pas divisible par 3 ou 5")
