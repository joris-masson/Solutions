NOM_FICHIER = "bottinNomPrenom.txt" #permet de pas avoir à réécrire le nom du fichier

def recherche(nom, prenom, file):
    fichier = open(file, 'r') #ouvre le fichier en lecture
    temp = [] #stockera nom, prenom, num
    nomTemp = '' #stockera le nom, pas vraiment besoin, mais plus lisible
    prenomTemp = '' #prenom
    numTemp = '' #num
    for element in fichier: #ligne après ligne
        temp = element.split() #coupe la string en plusieurs éléments de liste avec nom, prenom, num
        nomTemp = temp[0] #nom
        prenomTemp = temp[1] #prenom
        numTemp = temp [2] #num
        if (nomTemp == nom) and (prenomTemp == prenom):
            fichier.close() #ferme le fichier(avant le return(IMPORTANT))
            return numTemp #retourne le num
    fichier.close()
    return "" #retourne 'vide'
print(recherche("martin", "luc", NOM_FICHIER))

def rechercheNom(nom, file):
    fichier = open(file, 'r')
    temp = ''
    correspond = [] #pour stocker
    for element in fichier:
        temp = element.split()
        if temp[0] == nom: #si le nom correspond
            correspond.append(element) #ajoute la ligne complète à la liste
    fichier.close() #ferme le fichier
    return correspond
print(rechercheNom("dupont", NOM_FICHIER))

def combien(pre, file):
    fichier = open(file, 'r')
    numTemp = ''
    prefixTemp = ''
    nb = 0 #compteur
    for elem in fichier:
        numTemp = elem.split()[2] #split et prend le 3eme élément: le numéro
        prefixTemp = numTemp[:2] #prend les deux premiers char du numéro
        if prefixTemp == pre: #si le prefix est le bon
            nb += 1 #ajoute 1 au compteur
    return nb
print(combien('02', NOM_FICHIER))
