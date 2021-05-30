from tkinter import *

X,Y=20,20

def monquitter():
    fen.quit()
    fen.destroy()

def clavier(event):
    global X,Y
    touche=event.keysym
    print(touche)
    if touche=='Up':
        Y-=10
    elif touche=='Down':
        Y+=10
    elif touche == 'Right':
        X+= 10
    elif touche == 'Left':
        X-=10
    can.coords(carre, X-10,Y-10,X+10,Y+10)
    
fen=Tk()
fen.title("deplacement au clavier")

can=Canvas(fen,width=400, height=400,bg="white")
can.pack(side=LEFT)

carre=can.create_rectangle(X-10,Y-10, X+10, Y+10, fill="blue", outline='cyan')
can.bind('<KeyPress>', clavier)

can.focus_set()


bquitter=Button(fen, text='Q', command=monquitter)
bquitter.pack(side=BOTTOM)
fen.mainloop()
