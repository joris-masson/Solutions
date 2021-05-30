import random

def affiche(n):
    for i in range(n):
        print("*", end=' ')
    print("\n")

#pas besoin de faire min() puisque la f() existe déjà
    
def saisie(a, b):
    print("Entrez un entier entre ", a, "et ", b)
    rep = int(input())
    while (rep < a) or (rep > b):
        print("Entrez un entier entre ", a, "et ", b)
        rep = int(input())
    return rep

def quiCommence():
    joueur = random.randint(1, 2)
    print("Le joueur", joueur, "commence")
    return joueur

def quiJoue(joueurAct):
    if joueurAct == 1:
        return 2
    else:
        return 1
    
def saut(n):
    print("\n" * n)

def separateur(n):
    print("-" * n)

def main():
    joueur = quiCommence()
    nbAllumettes = 20
    nbMini = 1
    nbMaxi = 3
    aEnlever = 0
    print("Il y a", nbAllumettes, " allumettes, vous devez en retirer de", nbMini, "à", nbMaxi, "Celui qui tire la dernière allumette à perdu")
    print("Voici les allumettes: ")
    affiche(nbAllumettes)
    print("Bonne chance!")
    input("Appuyez sur 'entrée' pour continuer")
    saut(50)
    
    while nbAllumettes != 1:
        separateur(100)
        print("C'est le tour du joueur: ", joueur)
        affiche(nbAllumettes)
        if nbAllumettes < 3:
            if nbAllumettes == 3:
                aEnlever = saisie(1, 2)
            elif nbAllumettes == 2:
                aEnlever = saisie(1, 1)
        else:
            aEnlever = saisie(1, 3)
            
        nbAllumettes -= aEnlever
        joueur = quiJoue(joueur)
        separateur(100)
    print("Le joueur: ", joueur, "a perdu!")
        
main()
