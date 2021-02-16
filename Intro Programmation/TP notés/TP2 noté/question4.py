x = float(input("Note 1: "))
y = float(input("Note 2: "))
z = float(input("Note 3: "))

mentionVoulue = ''

noteMini = 0

sommeNote = x+y+z

moyenne = sommeNote/3
print("moyenne: ", moyenne)

if sommeNote >= 40:
    print("Bravo, impossible de ne pas valider.")
    mentionVoulue = input("Que voulez-vous comme mention TB, B, AB, P? ")
    if mentionVoulue == 'TB':
        if moyenne <= 16:
            print("Non, vous pouvez pas")
        else:
            print("C'est ok")

    if mentionVoulue == 'B':
        if moyenne <= 14:
            print("Non, vous pouvez pas")
        else:
            print("C'est ok")

    if mentionVoulue == 'AB':
        if moyenne <= 12:
            print("Non, vous pouvez pas")
        else:
            print("C'est ok")

    if mentionVoulue == 'P':
        if moyenne <= 10:
            print("Non, vous pouvez pas")
        else:
            print("C'est ok")
                          
    
elif sommeNote < 20:
    print("Dommage, vous ne pouvez plus valider.")
else:
    noteMini = 40 - sommeNote
    print("Vous pouvez le faire, c'est encore possible de valider. Il vous faudrat au moins", noteMini ,"la prochaine fois.")
    


