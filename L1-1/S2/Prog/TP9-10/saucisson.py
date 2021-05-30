from turtle import*

speed(-1)
color("red")
screen = Screen()
screen.setup(1000, 1000)

def lvl1(l):
    forward(l)

def avance(l):
    penup()
    lvl1(l)
    pendown()

def theSaucisson(n, l):
    if n == 0:
        lvl1(l)
    else:
        theSaucisson(n-1, l)
        right(90)
        theSaucisson(n-1, l)
        left(90)
        theSaucisson(n-1, l)
        left(90)
        theSaucisson(n-1, l)
        theSaucisson(n-1, l)
        right(90)
        theSaucisson(n-1, l)
        right(90)
        theSaucisson(n-1, l)
        left(90)
        theSaucisson(n-1, l)

theSaucisson(20, 3)
        
