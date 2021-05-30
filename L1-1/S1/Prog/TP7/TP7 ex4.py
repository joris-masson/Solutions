import random

def alea(n):
    return random.randint(1, n)

def auMoins(n):
    #face 1
    #pile 2
    nbPile = 0
    nbFace = 0
    lancer = 0
    try_ = 0
    while (nbPile <= n) and (nbFace <= n):
        lancer = alea(2)
        if lancer == 1:
            nbFace += 1
        else:
            nbPile += 1
        try_ += 1
    return try_

def main():
    n = int(input("valeur de n: "))
    print("Nombre d'essais pour obtenir ", n, "pile et face: ", auMoins(n))

main()
