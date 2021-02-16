from turtle import*
import random

speed(-1)
color("red")
screen = Screen()
screen.setup(1000, 1000)
left(90)

def lvl1(l):
    forward(l)
    backward(l)

def lvl2(l):
    lvl1(l)
    forward(l)
    left(60)
    lvl1(l/2)
    right(120)
    lvl1(l/2)
    left(60)
    backward(l)

def theArbre(n, l):
    if n == 0:
        lvl1(l)
    else:
        forward(l)
        left(60)
        theArbre(n-1, l/1.5)
        right(120)
        theArbre(n-1, l/1.5)
        left(60)
        backward(l)

theArbre(5, 150)
    
