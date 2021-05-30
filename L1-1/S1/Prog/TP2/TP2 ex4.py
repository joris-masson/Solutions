#Ce programme a été fait pour un dm de maths
from math import * #Importe de quoi calculer une racine carrée.

n = int(input("Combien d'équations voulez-vous vérifier? ")) #Demande le nombre d'équations à vérifier.

for i in range(n): #Va répéter n fois le code compris dans la boucle.
    a = float(input("a = ")) #Le programme demande à combien est égal "a", et l'assigne à a, une variable.
    b = float(input("b = ")) #Le programme demande à combien est égal "b", et l'assigne à b, une variable.
    c = float(input("c = ")) #Le programme demande à combien est égal "c", et l'assigne à c, une variable.

    d = (b * b) - 4 * a * c #Il calcule delta, et l'assigne à d, une variable

    print("Delta = ", d) #Il affiche Delta, au cas où.
    print() #Ceci sert à faire une ligne vide, pour plus de lisibilité.

    if d < 0: #Le programme vérifie si d est inférieur à 0.
        print("Delta < 0, donc il n'y a pas de solution") #Affiche le fait qu'il n'y ai pas de solution.
    if d > 0: #Il vérifie si d est supérieur à 0.
        x1 = (-b - sqrt(d)) / (2 * a) #Il calcule x1 et l'assigne à x1, une variable.
        x2 = (-b + sqrt(d)) / (2 * a) #Il calcule x2 et l'assigne à x2, une variable.
        print("x1 = ", x1, "x2 = ", x2) #Affiche x1 et x2.
    if d == 0: #Il vérifie si d est égal à 0.
        x0 = -b / (2 * a) #Il calcule x0 et l'assigne à x0, une variable.
        print("x0 = ", x0) #Affiche x0.
    print() #Ceci sert à faire une ligne vide, pour plus de lisibilité.

