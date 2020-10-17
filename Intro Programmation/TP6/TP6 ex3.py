import random

def somme(d):
    return d[0]+d[1]

def comptePoints(jeu):
    score = 0
    for elem in jeu:
        score += somme(elem)
    return score

def plus_cher(main):
    plusCher = (0,0)
    for d in main:
        if somme(d) >= somme(plusCher):
            plusCher = (d)
    return plusCher

def jouable(domino, plateau):
    if len(plateau) == 0: #plateau vide
        return True
    elif (domino[0] in plateau[-1]) or (domino[1] in plateau[-1]):
        return True
    else:
        return False

def DominosJouables(jeu, plateau):
    tupleJouable = ()
    for domino in jeu:
        if jouable(domino, plateau):
            tupleJouable += (domino),
    return tupleJouable

def choixOrdi(main, plateau):
    tupleJouable = DominosJouables(main, plateau)
    if len(tupleJouable) == 0:
        return False
    else:
        return plus_cher(tupleJouable)

def testPlateau(plateau):
    ancienDomino = ()
    for domino in plateau:
        if ancienDomino == ():
            pass
        else:
            if domino[0] != ancienDomino[1]:
                return False
        ancienDomino = domino
    return True

def creationJeu():
    dominos = ()
    for d1 in range(7):
        for d2 in range(7):
            dominos += (d1, d2),
    return dominos
