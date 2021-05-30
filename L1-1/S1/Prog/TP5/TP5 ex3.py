import random

def aleas(n):
    return random.randint(1, n)

def lancer(n):
    nbPile = 0
    
    for lancer in range(n):
        if aleas(2
                 ) == 2:
            nbPile += 1
    return nbPile

def main():
    nbLancer = int(input("Nombre de lancers: "))
    return lancer(nbLancer)

print(main())
