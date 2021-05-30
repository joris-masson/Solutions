import random

nbDeTour = int(input("Combien de tours voulez-vous faire? ")) #le nb de tour

resJoueur = 0
resOrdi = 0
tupleRes = () #Stocke les résultats du lancement des dés dans un tuple, pour pouvoir en simplifer le calcul du maximum

scoreJoueur = 0 #Score final du joueur
scoreOrdi = 0 #Score final de l'ordinateur

#Jeu
for tour in range(nbDeTour): #répète en f() du nb de tour, en gros ça représente un tour en entier
    print("----------tour: ", tour+1, "----------") #Affiche le tour actuel
    nbDeDes = int(input("Combien de dés voulez-vous lancer? ")) #Le nb de dés que le joueur et l'ordinateur vont lancer
    print("\n") #retour à la ligne

    resJoueur = random.randint((1*nbDeDes), (6*nbDeDes)) #lancement du joueur
    print("Vous avez fait ", resJoueur)
    resOrdi = random.randint((1*nbDeDes), (6*nbDeDes)) #lancement de l'ordi
    print("L'ordinateur a fait ", resOrdi, "\n")

    if (resJoueur > 21) or (resOrdi > 21): #si l'un des deux sont au dessus de 21
        if resJoueur > 21: #si c'est le joueur qui est au dessus
            print("Le joueur a dépassé 21, il perd donc deux points")
            scoreJoueur -= 2
        else: #sinon l'ordi
            print("L'ordinateur a dépassé 21, il perd donc deux points")
            scoreOrdi -= 2
    elif (resJoueur >= 21) and (resOrdi >= 21): #si les deux sont à 21 ou plus
        print("Les deux joueurs ont 21 ou plus, tour nul")
    elif (resJoueur == 21) or (resOrdi == 21): #si l'un des deux est à 21 tout pile
        if resJoueur == 21: #si c'est le joueur
            print("Le joueur a 21 tout pile, il gagne donc 5 points")
            scoreJoueur += 5
        else: #sinon l'ordi
            print("L'ordinateur a 21 tout pile, il gagne donc 5 points")
            scoreOrdi += 5
    else: #Quand les resultats sont inférieurs à 21
        print("Les deux joueurs ont moins de 21, le plus proche de 21 gagnera 2 points!")
        tupleRes = (resJoueur, resOrdi)
        if max(tupleRes) == resJoueur: #si le plus proche de 21 est le joueur
            print("Le joueur est le plus proche de 21, il gagne donc 2 points!")
            scoreJoueur += 2
        elif max(tupleRes) == resOrdi: #idem mais pour l'ordi
            print("L'ordinateur est le plus proche de 21, il gagne donc 2 points!")
            scoreOrdi += 2
        else: #quand les deux joueurs ont un résultat inférieurs à 21 et égal
            print("Les deux joueurs possèdent le même résultat, donc personne ne gagne de point")
    print("-----------------------------------")
    print("\n")

#Affichage des scores totaux
print("Le score du joueur est: ", scoreJoueur)
print("Le score de l'ordinateur est: ", scoreOrdi, "\n")

#Affichage du vainqueur
if scoreJoueur > scoreOrdi:
    print("Le joueur est donc vainqueur!")
elif scoreJoueur < scoreOrdi:
    print("L'ordinateur est donc vainqueur!")
else:
    print("C'est donc un match nul!")

