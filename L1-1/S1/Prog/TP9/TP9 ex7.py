import random

COULEURS = ('n', 'b', 'v', 'r')
HAUTEURS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
JOKER = ["j", "j"]

lePlateau = []
laPioche = []

mainJoueur1 = []
mainJoueur2 = []

def couple(l1, l2):
    return [[x, y] for x in l1 for y in l2]

def creation():
    jeu = couple(COULEURS, HAUTEURS)*2
    for i in range(2):
        jeu.append(JOKER)
    return jeu

def comptePoints(jeu):
    points = 0
    for carte in jeu:
        if carte == JOKER:
            points += 25
        else:
            points += carte[1]
    return points

def compatible(c1, c2):
    if c1 == JOKER or c2 == JOKER:
        return True
    elif (c1[0] != c2[0]) and (c1[1] != c2[1]):
        return False
    else:
        return True

def jouable(plateau, c1):
    return compatible(plateau[-1], c1)

def cartesJouables(plateau, jeu):
    jouables = []
    for carte in jeu:
        if jouable(plateau, carte):
            jouables.append(carte)
    return jouables

def pioche(joueur, n):
    global laPioche, mainJoueur1, mainJoueur2
    if joueur == '1':
        for carte in range(n):
            mainJoueur1.append(laPioche[-1])
            del laPioche[-1]
    elif joueur == '2':
        for carte in range(n):
            mainJoueur2.append(laPioche[-1])
            del laPioche[-1]

def distribue(nb):
    pioche('1', nb)
    pioche('2', nb)

def main():
    laPioche = creation()
    random.shuffle(laPioche)
    distribue(7)
