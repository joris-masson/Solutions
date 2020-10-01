import random

nbDeTour = int(input("Combien de tours voulez-vous faire? "))

resJoueur = 0
resOrdi = 0
tupleRes = ()

plusProche = ''

scoreJoueur = 0
scoreOrdi = 0

for tour in range(nbDeTour):
    print("tour: ", tour+1)
    resJoueur = 0
    resOrdi = 0
    nbDeDes = int(input("Combien de dés voulez-vous lancer? "))
    
    for joueur in range(nbDeDes):
        resJoueur += random.randint(1, 6)
    print("vous avez fait ", resJoueur)

    for ordi in range(nbDeDes):
        resOrdi += random.randint(1,6)
    print("L'ordinateur a fait ", resOrdi)

    if (resJoueur > 21) or (resOrdi > 21):
        if resJoueur > 21:
            print("Le joueur a dépassé 21, il perd donc deux points")
            scoreJoueur -= 2
        else:
            print("L'ordinateur a dépassé 21, il perd donc deux points")
            scoreOrdi -= 2
    elif (resJoueur >= 21) and (resOrdi >= 21):
        print("Les deux joueurs ont 21 ou plus, tour nul")
    elif (resJoueur == 21) or (resOrdi == 21):
        if resJoueur == 21:
            print("Le joueur a 21 tout pile, il gagne donc 5 points")
            scoreJoueur += 5
        elif resOrdi == 21:
            print("L'ordinateur a 21 tout pile, il gagne donc 5 points")
            scoreOrdi += 5
    else:
        print("Les deux joueurs ont moins de 21, le plus proche de 21 gagnera 2 points!")
        tupleRes = (resJoueur, resOrdi)
        if max(tupleRes) == resJoueur:
            print("Le joueur est le plus proche de 21, il gagne donc 2 points!")
            scoreJoueur += 2
        else:
            print("L'ordinateur est le plus proche de 21, il gagne donc 2 points!")
            scoreOrdi += 2
    print("\n")
print("Le score du joueur est: ", scoreJoueur, "\n")
print("Le score de l'ordinateur est: ", scoreOrdi, "\n")

if scoreJoueur > scoreOrdi:
    print("Le joueur est donc vainqueur!")
elif scoreJoueur < scoreOrdi:
    print("L'ordinateur est donc vainqueur!")
else:
    print("C'est donc un match nul!")

