import random

desMots1 = ("salut", "bonjour", "tartiflette", "fromage", "raclette", "lardon", "cool", "faim")
desMots2 = ("ouais", "pizza", "saucisse", "crème", "lit", "dormir")

tuples = (desMots1, desMots2)

leTuple = 0 #tuple à étudier

erreur = 0

def copie(mot):
    motEntre = ''
    nbEssais = 0
    while True:
        print("recopie ce mot: ", mot)
        motEntre = input().strip()
        if (motEntre == mot) or (nbEssais >= 5):
            break
        else:
            nbEssais += 1
    return nbEssais

def suiteMots(tupleMots):
    nbErreursTotal = 0
    for mot in tupleMots:
        nbErreursTotal += copie(mot)
    return nbErreursTotal

erreur = suiteMots(desMots1)
if erreur <= 1:
    print("Bravo")
else:
    print("Dommage")
