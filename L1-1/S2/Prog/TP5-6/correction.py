from tkinter import *
from random import *
import pickle

# variables globales 
#valeurs par défaut à lire dans le dictionnaire 

dicoVal={"tailleCase":20, "x0":50, "y0":50, "tailleGrille":24, "dessinM":""}
c=dicoVal["tailleCase"] # dimension d'une case supposée carrée
x0,y0=dicoVal["x0"],dicoVal["y0"]  #coordonnées du point en haut à gauche
n=dicoVal["tailleGrille"] #taille de la grille
m=dicoVal["dessinM"]  # le dessin

crayon="+"

couleur={"+":"black", "_": "white", "*":"orange"}

def creegrille(n, x):
    res=[0]*n
    for i in range(n):
        res[i]= [x]*n
    return res

#  fonctions Tkinter

def retour():  # pour l'instant quitte l'appli et met le dessin en cours dans le dictionnaire puis sauvegarde ce dictionnaire.
    dicoVal["murs"]=m
    ecriture(dicoVal,"fichierDico")
    dessin.quit()
    dessin.destroy()

def dessineGrille(m):#dessin de la grille grâce au dico couleur qui fait la correspondance entre le symbole de la grille python et la couleur
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

            

#fonction associée au clic pour dessiner une case
                
def murs(event):  # gèer affichage du clic et mise à jour de la grille grâce au dico couleur qui fait la correspondance entre le symbole de la grille pythpn et la couleur du dessin
    [i,j]=correspond(event.x,event.y)
    can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur[crayon])
    m[i][j]=crayon


    
    
        
def correspond(x,y):  # transforme la position du clic en case de la grille  attention  à ne pas inverser x et y
    return [(y-y0)//c,(x-x0)//c]


# fonctions des boutons
def sauve():
    zoneSaisie.delete("0",END)
    cadre.pack()
    zoneSaisie.bind('<Return>', sauvegarde)

def sauvegarde(event):
    nom=zoneSaisie.get()
    ecriture(m,nom)
    zoneSaisie.unbind('<Return>')
    cadre.pack_forget()

def charge():
    zoneSaisie.delete("0",END)
    cadre.pack()
    zoneSaisie.bind('<Return>', chargement)

def chargement(event):
    nom=zoneSaisie.get()
    global m
    m=lit(nom)
    zoneSaisie.unbind('<Return>')
    cadre.pack_forget()
    dessineGrille(m)
    
def gomme():
    global crayon
    crayon="_"
    bg.configure(bg="green")
    bm.configure(bg="light grey")
    

def murNoir():
    global crayon
    crayon="+"
    bm.configure(bg="green")
    bg.configure(bg="light grey")
    

def commencer():
    global m, crayon
    crayon='+'
    m=creegrille(n,'_')
    dessineGrille(m)
    print(m)
    can.bind("<Button-1>",murs)


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




## définitions positionnement des widgets
    
dessin=Tk()
dessin.title("jeu")

# canvas
can= Canvas(dessin,height=600,width=600,bg="white")
can.pack(side=LEFT)

# bouton commencer/recommencer
bnew=Button(dessin,text="commencer/recommencer",command=commencer,font=("Ubuntu",20,"bold"))
bnew.pack(side=TOP,pady=50)

# bouton de sauvegarde
bs=Button(dessin,text="sauvegarde",command=sauve,font=("Ubuntu",20,"bold"))
bs.pack(side=TOP,pady=50)

# cadre pour mettre zone de saisie et laber associé
cadre=Frame(dessin) 
lab=Label(cadre, text=" saisir le nom du fichier :")
lab.pack()
zoneSaisie=Entry(cadre, width=15)
zoneSaisie.pack()


# bouton de chargement
bc=Button(dessin,text="charger",command=charge,font=("Ubuntu",20,"bold"))
bc.pack(side=TOP,pady=50)

# bouton retour
bq=Button(dessin,text="retour",command=retour,font=("Ubuntu",20,"bold"))
bq.pack(side=BOTTOM,pady=50)  

# zone de choix gomme/crayon/etc
CadreCrayon=Frame(dessin, bg="cyan")
CadreCrayon.pack(side=BOTTOM, pady=50)

bg=Button(CadreCrayon,text="gomme",command=gomme, font=("Ubuntu",20,"bold"))
bg.pack(side=LEFT)
bm=Button(CadreCrayon,text="mur",bg="green",command=murNoir, font=("Ubuntu",20,"bold"))
bm.pack(side=LEFT)
cadre.pack()


dessin.mainloop()
