############################
# JEU DU NOMBRE MYSTERIEUX #
############################

from tkinter import *
from random import *

def jouer():
    global cp
    cp=cp+1
    ch=entree.get()
    entree.delete(0,END)
    try :
        nb=int(ch)
    except ValueError:
        pass  #il ne se passe rien si la saisie ne peut pas être transformée en entier
               # en particulier si vide
    else:
        if nb==x:
            larep.insert(END, "%s bravo vous gagnez en %s coups \n" %(nb,cp))
            bnew.configure(state=ACTIVE)
            bv.configure(state=DISABLED)
            bp.configure(state=DISABLED)
        elif nb<x:
            larep.insert(END, "%s :  trop petit \n" %nb)   
        else:
            larep.insert(END, "%s  :  trop grand\n" %nb)
def paresseux():
    larep.insert(END, " paresseux!!! il fallait trouver %s \n" %(x))
    bnew.configure(state=ACTIVE)
    bv.configure(state=DISABLED)
    bp.configure(state=DISABLED)

def new():
    global cp
    global x
    cp=0
    x=randint(1,100)
    larep.delete("0.0",END)
    bv.configure(state=ACTIVE)
    bp.configure(state=ACTIVE)
    bnew.configure(state=DISABLED)
    
def monquitter():
    fen.quit()
    fen.destroy()

mafonte=("ubuntu", 16, "bold")
x=randint(1,100)
cp =0

fen = Tk()
fen.title("jeu du nombre mystérieux: devinez un entier compris entre 1 et 100")
fen.geometry("750x750")
saisie=Frame(fen)
saisie.pack()
ch=Label(saisie, text= "entrez votre nombre",fg="blue",font=mafonte)
ch.pack(side=LEFT, padx=10)
entree=Entry(saisie,font=mafonte, width=6)
entree.pack(side=LEFT, padx=10)
bv=Button(saisie,text="OK",font=mafonte,command=jouer)
bv.pack(side=LEFT, padx=10)
bp=Button(saisie,text="abandon",font=mafonte,command=paresseux)
bp.pack(side=LEFT, padx=50)


bq=Button(fen,text="quitter",font=mafonte,command=monquitter)
bq.pack(side=BOTTOM)
bnew=Button(fen,text="nouvelle partie",font=mafonte,command=new)
bnew.pack(side=BOTTOM)
bnew.configure(state=DISABLED)

larep=Text(fen,width= 60,height=20,bg="light grey",font=mafonte, padx=20)
larep.pack()


def f(i):
    g=lambda: entree.insert(END, str(i))
    return g


pave=Frame(fen)
pave.pack(side=RIGHT)

ligne1=Frame(pave)
ligne1.pack()
ligne2=Frame(pave)
ligne2.pack()
ligne3=Frame(pave)
ligne3.pack()
ligne4=Frame(pave)
ligne4.pack(side=TOP)


Button(ligne4, text="0", command=f(0)).pack(side=LEFT)
for i in range(1,10):
    if i<4:
        Button(ligne1, text=str(i), command=f(i)).pack(side=LEFT)
    elif i<7:
        Button(ligne2, text=str(i), command=f(i)).pack(side=LEFT)
    else:
        Button(ligne3, text=str(i), command=f(i)).pack(side=LEFT)

fen.mainloop()

