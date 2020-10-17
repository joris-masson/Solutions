desMots1 = ("bonjour", "salut", "au revoir", "j'ai faim", "alors", "j'ai pas faim", "j'ai soif", "manger", "mourir")
desMots2 = ("mourir", "alors", "vivre", "le café", "porte", "chien", "ouaf ouaf", "miaou", "chat", "bonbon", "burger", "pizza", "raclette", "tartiflette", "12345678901")

def compare_nb(l1, l2):
    nbEgaux = 0
    for elem1 in l1:
        for elem2 in l2:
            if elem1 == elem2:
                nbEgaux += 1
    return nbEgaux

def compare(l1, l2):
    tupleEgaux = ()
    for elem1 in l1:
        for elem2 in l2:
            if elem1 == elem2:
                tupleEgaux += (elem2,)
    return tupleEgaux

def fusion(l1, l2):
    tupleFusion = ()
    for elem1 in l1:
        tupleFusion += (elem1,)
    for elem2 in l2:
        if elem2 not in tupleFusion:
            tupleFusion += (elem2,)
    return tupleFusion

def motpluslong(listemots):
    tailleMaxMot = 0
    tupleMax = ()
    for elem in listemots:
        if len(elem) >= tailleMaxMot:
            tailleMaxMot = len(elem)
    for elem in listemots:
        if len(elem) == tailleMaxMot:
            tupleMax += (elem,)
    return tupleMax

print(motpluslong(desMots2))
