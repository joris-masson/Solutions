from tkinter import *
detect=False
X=20
Y=20
def monquitter():
    fen.quit()
    fen.destroy()

def drag(event):
    X,Y=event.x, event.y
    if detect:
        if X<0:
            X=0
        if X>400:
            X=400
        if Y<0:
            Y=0
        if Y>400:
           Y=400
    can.coords(carre, X-10, Y-10, X+10, Y+10)

def clic(event):
    global detect
    X,Y=event.x, event.y
    [xmin,ymin,xmax,ymax]=can.coords(carre)
    if xmin<=X<=xmax and ymin<=Y<=ymax :
        detect=True
    else:
        detect=False
    
fen=Tk()
fen.title("drag and drop")

can=Canvas(fen,width=400, height=400,bg="white")
can.pack(side=LEFT)

carre=can.create_rectangle(X-10, Y-10, X+10, Y+10, fill="blue", outline='cyan')
can.bind('<Button-1>', clic)
can.bind('<B1-Motion>', drag)

bquitter=Button(fen, text='Q', command=monquitter)
bquitter.pack(side=BOTTOM)
fen.mainloop()
