from tkinter import *

def monquitter():
    fen1.quit()
    fen1.destroy()

def entree1(event):
    texto.delete(0,END)
    texto.insert(END,"survol de la zone bleue")
def sortie1(event):
    texto.delete(0,END)
    texto.insert(END,"on quitte la zone bleue")

def entree2(event):
    texto.delete(0,END)
    texto.insert(END,"survol de la zone rose")
def sortie2(event):
    texto.delete(0,END)
    texto.insert(END,"on quitte la zone rose")        
    
fen1 = Tk()


can=Canvas(fen1)
can.pack(side=LEFT, padx=20, pady=10)
zone1=Frame(can, width=50, height=50,bg="cyan")
zone2=Frame(can, width=50, height=50,bg="pink")
zone1.pack(side=LEFT, padx=10)
zone2.pack(side=LEFT)

texto=Entry(fen1, width=30)
texto.pack(padx=10)

zone1.bind("<Enter>",entree1)
zone1.bind("<Leave>",sortie1)
zone2.bind("<Enter>",entree2)
zone2.bind("<Leave>",sortie2)


boutonQuitter = Button(fen1, text='Quitter', command = monquitter)
boutonQuitter.pack(side=BOTTOM)
fen1.mainloop()
