import random

def alea(n):
    return random.randint(1, n)

def calcul(n):
    a = alea(n)
    b = alea(n)
    print("Calculez la somme de ", a, "et ", b, ": ")
    calculUser = int(input())
    if calculUser == a+b:
        print("Bravo")
        return 1
    else:
        print("Non, c'est : ", a+b)
        return 0

def serie_calcul(n, nb):
    nbBonnesReponses = 0
    res = 0
    for calc in range(nb):
        res = calcul(nb)
        if res == 1:
            nbBonnesReponses += 1
    return nbBonnesReponses

def main():
    n = int(input("Jusqu'à combien iront les nombres? "))
    nb = int(input("Et combien de calculs voulez-vous faire? "))
    score = serie_calcul(n, nb)
    return score

print("Score: ", main())
