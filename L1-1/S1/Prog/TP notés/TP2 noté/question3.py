x = float(input("Note 1: "))
y = float(input("Note 2: "))
z = float(input("Note 3: "))

noteMini = 0

sommeNote = x+y+z

if sommeNote >= 40:
    print("Bravo, impossible de ne pas valider.")
elif sommeNote < 20:
    print("Dommage, vous ne pouvez plus valider.")
else:
    noteMini = 40 - sommeNote
    print("Vous pouvez le faire, c'est encore possible de valider. Il vous faudrat au moins",noteMini ,"la prochaine fois.")
    

moyenne = sommeNote/3
print("moyenne: ", moyenne)
