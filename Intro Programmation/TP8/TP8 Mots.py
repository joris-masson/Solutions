import random

desMots1 = ["ohhhhh", "tartiflette", "raclette", "gouda", "jambon", "saucisson"]
desMots2 = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit"]

def compteMots(n, listeMots):
    nbMots = 0
    for mot in listeMots:
        if len(mot) >= n:
               nbMots += 1
    return nbMots

def commencePar(cara, listeMots):
    listeDeMots = []
    for mot in listeMots:
        if mot[0] == cara:
            listeDeMots.append(mot)
    return listeDeMots

def motPlusLong(listeMots):
    plusLong = 0
    listeDeMots = []
    for mot in listeMots:
        if len(mot) > plusLong:
            plusLong = len(mot)
    for mot in listeMots:
        if len(mot) == plusLong:
            listeDeMots.append(mot)
    return listeDeMots[random.randint(0, len(listeDeMots))]

def petiteLongueur(listeMots):
    plusCourt = 10**9
    for mot in listeMots:
        if len(mot) < plusCourt:
            plusCourt = len(mot)
    return plusCourt

def plusPetitsMots(listeMots):
    plusPetit = 10**9
    listeDeMots = []
    for mot in listeMots:
        if len(mot) < plusPetit:
            plusPetit = len(mot)
    for mot in listeMots:
        if len(mot) == plusPetit:
            listeDeMots.append(mot)
    return listeDeMots

def recopie(mot):
    rep = ''
    nbEssais = 0
    while rep != mot:
        print("Vous devez recopier ce mot: ", mot)
        rep = supprimeEspaces(input().lower())
        nbEssais += 1
        if nbEssais == 5:
            print("Pas plus de 5 essais, dommage")
            break
        
        if rep == mot:
            print("\nC'est bien!")
        else:
            print("\nC'est pas bien!")
    print("Vous avez mis", nbEssais, "essais à recopier(ou non) ce mot")
    return nbEssais

def supprimeAvant(mot):
    return mot.stripl()

def supprimeApres(mot):
    return mot.stripr()

def supprimeEspaces(mot):
    return mot.replace(' ', '')

def test(listeMots):
    nbEssaisTotal = 0
    for mot in listeMots:
        nbEssaisTotal += recopie(mot)
    print("Vous avez fait ", (nbEssaisTotal - len(listeMots)), "erreur(s)")

test(desMots2)
