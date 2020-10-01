a = int(input("Angle a = "))
b = int(input("Angle b = "))
c = int(input("Angle c = "))

if (a + b + c) != 180:
    print("Ce n'est pas un triangle")
    
elif (a == 0) or (b == 0) or (c == 0):
    print("C'est un triangle dégénéré")
    
elif (a == b) and (b == c):
    print("C'est un triangle équilatéral")
    
elif ((a == 90) or (b == 90) or (c == 90)) and ((a == b) or (a == c) or (b == c)):
    print("C'est un triangle isocèle rectangle")
    
elif (a == 90) or (b == 90) or (c == 90):
    print("C'est un triangle rectangle")
    
elif (a == b) or (a == c) or (b == c):
    print("c'est un triangle isocèle")
    
else:
    print("C'est un triangle quelconque")
