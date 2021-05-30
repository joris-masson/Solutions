from simplification import grille

ex = [ ['P','Y','T','H','O','N'] , ['R','*','A','U','M','A'], ['O','M','B','R','E','*'], ['G','A','L','E','T','S'], ['*','T','E','*','S','U']]

grille.afficheGrille(ex) #affiche la grille d'exemple

def uneLettre(maGrille):
    for ligne in maGrille:
        for elem in ligne:
            if len(elem) > 1: #si la taille d'un élément de la ligne est supérieur à 1
                return False #ça retourne faux
    return True #si aucun des élément ne fait plus de 1 char

def retourneLigne(maGrille, ligne):
    return ''.join(maGrille[ligne]) #permet de créer une string à partir de la liste ligne

def retourneColonne(maGrille, colonne):
    #fait pareil qu'en haut, mais lis et inscrit dans une liste l'élément 'colonne'
    lettres = []
    for colonnes in maGrille:
        lettres.append(colonnes[colonne])
    return ''.join(lettres)

def recupereLignes(maGrille):
    mots = []
    for ligne in range(len(maGrille)): #se répète autant de fois qu'il y a de lignes dans la grille
        mots.append(retourneLigne(maGrille, ligne))
    return mots

def recupereColonnes(maGrille):
    mots = []
    for colonne in range(len(maGrille[0])): #se répète autant de fois qu'il y a de colonnes dans la grille
        mots.append(retourneColonne(maGrille, colonne))
    return mots

def enleveEtoiles(mot):
    tempMot = '' #permet de stocker un mot temporairement
    listeMots = []
    for lettre in mot:
        if lettre != '*':
            tempMot += lettre #rajoute chaque lettre au mot si * n'est pas rencontré
        else:
            listeMots.append(tempMot) #rajoute le mot
            tempMot = '' #et vide le stockage temporaire
    listeMots.append(tempMot) #permet de rajouter le dernier mot enregistré
    if listeMots[0] == '':
        listeMots.remove(listeMots[0]) #permet de retirer le premier élément de la liste s'il est vide
    return listeMots

def ecreme(liste):
    newL = []
    for elem in liste: #passe en revu chaque élément et vérifie que ça longueur est > à 1
        if len(elem) > 1:
            newL.append(elem)
    return newL

def listeMots(maGrille):
    #pas encore fait
    pass
            
print(ecreme([ 'UN' , 'EXEMPLE' , ' ' , 'A' , 'TRAITER' , '!' ]))
