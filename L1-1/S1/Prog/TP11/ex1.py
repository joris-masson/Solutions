def creeGrille(lignes, colonnes):
    grille = lignes * [0] #crée 'lignes' [0]
    for colonne in range(len(grille)): #répète selon le nb de lignes que possède la grille
        grille[colonne] = [0] * colonnes #"édite" chaque élément(qui était avant [0]) de la grille, pour le remplacer par 'colonnes' [0]
    return grille

def isZero(grille):
    res = 0
    for ligne in grille: #boucle qui fait la somme de chaque ligne de la grille
        res += sum(ligne)
    if res == 0: #et vérifie ensuite si la somme de toute les lignes est égale à 0
        return True #si oui
    else:
        return False #si non
    
def afficheGrille(grille):
    for ligne in grille: #'ligne' prend la valeur de chaque ligne de la grille successivement
        for elem in ligne: #et 'elem' prend ensuite la valeur de chaque élément de 'ligne' successivement
            print(elem, end=' ') #affiche un élément, puis fait un espace
        print() #saute une ligne(le print a par défaut un end="\n")

def compte(grille, val):
    res = 0
    for ligne in grille:
        for elem in ligne:
            if elem == val: #si un élément est égal à val
                res += 1 #on incrémente
    return res

def sommeGrille(grille): #pas par indice(parce que c'est long et chiant)
    res = 0
    for ligne in grille:
        res += sum(ligne) #ajoute la somme de la ligne à res
    return res

ex =[[ 5 , 10 , 4 , 7 ] , [ 7 , 8 , 2 , 4 ] , [ 0 , 0 , 9 , 8 ] , [ 1 , 9 , 6 , 3 ] , [ 8 , 0 , 10 , 6 ]] #grille d'exemple donnée par la prof

def casesZero(grille):
    cases = []
    #variables qui permettent de ne pas passer par un parcours avec indice, elles représentent des coordonnées, x -> colonne; y -> ligne
    x = -1 #si définie à 0, il y a un décalage d'1
    y = -1 #idem
    for ligne in grille:
        y += 1 #on passe une ligne, on ajoute 1 à y
        x = -1 #on redéfini x à -1
        for elem in ligne:
            x += 1 #on passe une colonne, on ajoute 1 à x
            if elem == 0: #si un élément est égal à 0
                cases.append([x, y]) #on ajoute le couple de coordonnées correspondant
    return cases

afficheGrille(ex)
print(casesZero(ex))
