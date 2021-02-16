from tkinter import *
from random import *
from copy import *

# variables globales
# exemples de murs (provisoire)
exemple=[['_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', 0, '_', '_', '_', '_', '_', '_', '_', 1, 0, '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '_'], ['_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_'], ['_', '_', '_', '_', '_', '_', '+', '+', '+', '+', '+', '+', '+', '+', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_'], ['_', '_', '+', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_'], ['_', '_', '+', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '+', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '+', '+', '+', '+', '+', '_', '_', '_'], ['_', '_', '+', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '+', '_', '_', '_', '+', '_', '_', '_'], ['_', '_', '+', '+', '+', '+', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '+', '_', '_', '_', '+', '+', '+', '_'], ['_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_', '_', '+', '_', '_', '_', '+', '_', '_', '_'], ['_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_', '_', '+', '_', '_', '_', '+', '_', '_', '_'], ['_', '_', '_', '_', '+', '_', '_', '_', '_', '+', '+', '+', '+', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_'], ['_', '_', '_', '_', '+', '_', '_', '_', '_', '+', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_'], ['_', '_', '_', '_', '+', '_', '_', '_', '_', '+', '_', '_', '_', '+', '+', '+', '+', '+', '+', '+', '+', '_', '_', '_'], ['_', '_', '_', '_', '+', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '+', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_', '_', '_', '_', '+', '_', '_', '_', '_', '_'], ['_', '_', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 1, '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]

#valeurs par défaut à lire dans le dictionnaire 

dicoVal={"tailleCase":20, "x0":50, "y0":50, "tailleGrille":24, "dessinM":exemple,  "nbfantomes":10, "nbtresors":10}

c=dicoVal["tailleCase"] # dimension d'une case supposée carrée
x0,y0=dicoVal["x0"],dicoVal["y0"]  #coordonnées du point en haut à gauche
n=dicoVal["tailleGrille"] #taille de la grille
m=dicoVal["dessinM"]  # le dessin des murs en cours

# position du joueur
pos=(0,0)
exemple[pos[1]][pos[0]] = '*'


# dico pour dessiner  (commun plusieurs modules)
couleur={"+":"black", "_": "white", "*":"orange", 1:"light green", 0:"blue"}

# fonction de essin de l agrille du fichier des murs
def ZeDessineGrille(m):#dessin de la grille grâce au dico couleur qui fait la correspondance entre le symbole de la grille python et la couleur
    can.delete(ALL)
    n=len(m)
    for i in range(n+1):  # dessin des traits de la grille
        can.create_line(x0+c*i, y0,x0+c*i,y0 + n*c)
        can.create_line(x0, y0+c*i,x0+n*c ,y0+c*i)

    for i in range(n):  # coloriage des cases murs non vides
        for j in range(n):
            x=m[i][j]
            if x!='_':
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur[x])    

            


def creeGrille(n, x):
    res=[0]*n
    for i in range(n):
        res[i]= [x]*n
    return res


def aleagrille():  
    return ""
    # à écrire

def deplacement(m,d):# deplacement de d à partir de la position pos  version tresor/fantômes/murs
    global pos
    lastPos = pos
    if d == 'H':
        pos = (pos[0], pos[1]-1)
        print("haut")
        print(pos)
    elif d == 'B':
        pos = (pos[0], pos[1]+1)
        print("bas")
        print(pos)
    elif d == 'D':
        pos = (pos[0]+1, pos[1])
        print("droite")
        print(pos)
    else:
        pos = (pos[0]-1, pos[1])
        print("gauche")
        print(pos)
    updateJoueur(lastPos)
    ZeDessineGrille(m)
    return ""
   # à écrire
    

def changeScore(p):
    score = txt.get()
    score += 1
    txt.delete()
    affiche(score)
    return ""
   # à écrire

def arrive():
    return ""
    # à écrire

#  fonctions Tkinter
def monquitter():
    dessin.quit()
    dessin.destroy()


# les 4 fonctions de déplacement    
def H():
    deplacement(m, 'H')
    dessineGrille(m)
    
def D():
    deplacement(m, 'D')
    dessineGrille(m)
    
def G():
    deplacement(m, 'G')
    dessineGrille(m)
    
def B():
    deplacement(m, 'B')
    dessineGrille(m)
    
def dessineGrille(m):  # version carrés de couleurs
    return ""
   # à écrire
   
def affiche(mess):
    txtMess.delete("0.0",END)
    txtMess.insert(END, mess)

def bouge(event): # pour se déplacer avec les touches de direction
    return ""
    # à écrire

def updateJoueur(lastPos):
    global pos
    exemple[lastPos[1]][lastPos[0]] = '_'
    exemple[pos[1]][pos[0]] = '*'
    return 0
    
def new():
    global m, pos
    ZeDessineGrille(m)
    return ""
   # à écrire
            
## et les widgets
    
dessin=Tk()
dessin.title("jeu")


can= Canvas(dessin,height=600,width=600,bg="white")
can.pack(side=LEFT)


bjouer=Button(dessin,text="jouer",command=new,font=("Ubuntu",20,"bold"))
bjouer.pack(side=TOP)



cadre=Frame(dessin, pady=50, width=160)
BH=Button(cadre, command=H, text='H',font=("Ubuntu",20,"bold"))
BH.pack()
cadremilieu=Frame(cadre)
cadremilieu.pack()
BG=Button(cadremilieu, command=G, text='G',font=("Ubuntu",20,"bold"))
BD=Button(cadremilieu, command=D, text='D',font=("Ubuntu",20,"bold"))
BB=Button(cadre, command=B, text='B',font=("Ubuntu",20,"bold"))
cadre.pack()

BG.pack(side=LEFT)
BD.pack(side=LEFT)
BB.pack()

bq=Button(dessin,text="Quitter",command=monquitter,font=("Ubuntu",20,"bold"))
bq.pack(side=BOTTOM)

cadreScore=Frame(dessin, pady=50, padx=20)
lab=Label(cadreScore, text= "votre score",font=("Ubuntu",20,"bold"))
txt=Text(cadreScore, height=1, width=4,font=("Ubuntu",20,"bold"))
lab.pack(side=LEFT)
txt.pack(side=LEFT)

cadreMessage=Frame(dessin, pady=50, padx=20)
cadreMessage.pack(side=BOTTOM)
labMess=Label(cadreMessage, text= "informations",font=("Ubuntu",20,"bold"))
txtMess=Text(cadreMessage, height=2, width=20,font=("Ubuntu",18,"bold"))
labMess.pack(side=TOP)
txtMess.pack(side=TOP)

dessin.mainloop()
