def creeGrille(lignes, colonnes):
    grille = lignes * [0] #crée 'lignes' [0]
    for colonne in range(len(grille)): #répète selon le nb de lignes que possède la grille
        grille[colonne] = [0] * colonnes #"édite" chaque élément(qui était avant [0]) de la grille, pour le remplacer par 'colonnes' [0]
    return grille

def afficheGrille(grille):
    for ligne in grille: #'ligne' prend la valeur de chaque ligne de la grille successivement
        for elem in ligne: #et 'elem' prend ensuite la valeur de chaque élément de 'ligne' successivement
            print(elem, end=' ') #affiche un élément, puis fait un espace
        print() #saute une ligne(le print a par défaut un end="\n")
