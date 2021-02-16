from tkinter import *
from random import *
import pickle

# variables globales 
#valeurs par défaut à lire dans le dictionnaire 

dicoVal={"tailleCase":20, "x0":50, "y0":50, "tailleGrille":30, "dessinM":"", "crayon":1}
c=dicoVal["tailleCase"] # dimension d'une case supposée carrée
x0,y0=dicoVal["x0"],dicoVal["y0"]  #coordonnées du point en haut à gauche
n=dicoVal["tailleGrille"] #taille de la grille
m=dicoVal["dessinM"]  # le dessin des murs en cours
crayon=dicoVal["crayon"] # si la gomme est à 0 on dessine un mur sinon on dessine une case vide
grille = []

#  fonctions grille
def creeGrille(n, x):
    res=[0]*n
    for i in range(n):
        res[i]= [x]*n
    return res

def afficherGrille(grille):
    global c, n
    for x in range(n):
        can.create_line(x*c, 0, x*c, 600)
    for y in range(n):
        can.create_line(0, y*c, 600, y*c)

def changerCase(coord, valeur):
    global c, grille, crayon
    coord = (int(coord[1]//c), int(coord[0]//c))
    print(coord)
    print(grille[coord[0]][coord[1]])
    grille[coord[0]][coord[1]] = valeur
    print(grille)
    if crayon == 1:
        can.create_rectangle(coord[1]*c, coord[0]*c, (coord[1]*c+c), (coord[0]*c+c), fill='black')
    elif crayon == 0:
        can.create_rectangle(coord[1]*c, coord[0]*c, (coord[1]*c+c), (coord[0]*c+c), fill='white')

#  fonctions Tkinter
# à compléter

#fonction associée au clic pour dessiner une case
# à compléter
def clic(event):
    global crayon
    coord = getCoord(event)
    print(coord, crayon)
    changerCase(coord, crayon)
    
def getCoord(event):
    coord = (event.x, event.y)
    return coord

# fonctions des boutons
# à compléter
def commencer():
    global n, grille, c
    can.create_rectangle(0,0, 600, 600, fill='white')
    grille = creeGrille(n, 0)
    print(grille)
    afficherGrille(grille)

def switchGomme():
    global crayon
    if crayon == 0:
        crayon = 1
    else:
        crayon = 0
    print(crayon)
        
# fonctions pickle
def ecriture(l,f):
    p=open(f, "wb") # sauvegarde dans f
    pickle.dump(l,p)
    p.close()

def lit(f):
    p=open(f,"rb")
    truc= pickle.load(p)
    p.close()
    return truc

## définitions et positionnement des widgets

dessin=Tk()
dessin.title("jeu")

# canvas
can= Canvas(dessin,height=600,width=600,bg="white")
can.pack(side=LEFT)

# bouton commencer/recommencer
# à compléter
commencer = Button(dessin, text="Commencer/Recommencer", command=commencer)
commencer.pack()

# bouton de sauvegarde
# à compléter
save = Button(dessin, text="Sauvegarder")
save.pack()

# cadre pour mettre zone de saisie et label associé
# à compléter
cadreSaisie = Frame(dessin, borderwidth=3, relief=GROOVE)
labelSaisie = Label(cadreSaisie, text="test")
saisie = Entry(cadreSaisie, textvariable='Oui')

cadreSaisie.pack()
labelSaisie.pack()
saisie.pack()

# bouton de chargement
# à compléter
chargement = Button(dessin, text = "Charger")
chargement.pack()

# bouton retour
# à compléter
retour = Button(dessin, text = "Retour", command=dessin.quit)
retour.pack()

# bouton gomme/crayon
# à compléter
gomme = Button(dessin, text="Crayon/Gomme", command=switchGomme)
gomme.pack()

can.bind("<Button-1>", clic)
dessin.mainloop()
