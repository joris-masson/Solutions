import random

def tirage():
    return random.randint(0, 5)

def serie(n):
    tir = 0
    nb = [0]*6
    for lancer in range(n):
        tir = tirage()
        nb[tir] += 1
    return nb

def convertList2Str(l):
    return [str(elem) for elem in l]

def affiche(l):
    print(' '.join(convertList2Str(l)))

def somme(l1, l2):
    return [l1[i]+l2[i] for i in range(len(l1))]

def serieMult(n):
    rep = ''
    resTotal = [0]*6
    while rep != 'n':
        resTotal = somme(resTotal, serie(n))
        affiche(resTotal)
        rep = ''
        while (rep != 'n') and (rep != 'o'):
            rep = input("Voulez-vous continuer? (o/n) ")
    
print(serieMult(100))
