#travail pour une grille

from tkinter import *
from random import *

nb= 8 # nombre de cases (grille carree)
c=50 # dimension d'une case supposée carrée
x0,y0=20,20  #coordonnées du point en haut à gauche

tresor=[randint(0,7),randint(0,7)]
trouve=0   # pour arreter le jeu quand le trésor est trouvé

fonte=("ubuntu", 14, "bold")
def monquitter():
    dessin.quit()
    dessin.destroy()

def grille():
    for i in range(nb+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + nb*c)
        can.create_line(x0, y0+c*i,x0+nb*c ,y0+c*i)

def jouer(event):
    global trouve
    if not trouve:  # sert à ne pas continuer après qu'on ait trouvé le trésor
        [i,j]=correspond(event.x,event.y)
        if i in range(nb) and j in range (nb):   # on ne fait rien si le click est hors grille
            can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=coul(i,j))
            if  [i ,j] == tresor:
                trouve=1
                t.pack(side=BOTTOM)
                t.insert(END,"BRAVO")
                b2.configure(state=ACTIVE)
             

def correspond(x,y):
    return [(y-y0)//c,(x-x0)//c]

def coul(i,j):
    [x,y]=tresor
    d= max(abs(x-i),abs(y-j))
    if d== 0:
        return "red"
    elif d==1:
        return "orange"
    elif d==2:
        return "yellow"
    elif d==3:
        return "green"
    else:
        return "blue"

def new():
    global tresor
    global trouve
    trouve=0
    t.pack_forget ()
    tresor=[randint(0,7),randint(0,7)]
    t.delete("0.0",END)
    can.delete(ALL)
    grille()
    b2.configure(state=DISABLED)  # le bouton demarrer devient inactif



dessin=Tk()
Label(dessin,text="Jeu du tresor",font=fonte,fg="blue").pack()


can= Canvas(dessin,height=500,width=500,bg="white")
can.pack(side=LEFT)


b2=Button(dessin,text="demarrer une partie",command=new,font=fonte)
b2.pack(side=TOP)
b1=Button(dessin,text="Quitter",command=monquitter,font=fonte)
b1.pack(side=BOTTOM)



t=Text(dessin ,height=1,width=7,bg="light grey",fg="red",font=("ubuntu",30,"bold"))


can.bind("<Button-1>",jouer)

dessin.mainloop()

