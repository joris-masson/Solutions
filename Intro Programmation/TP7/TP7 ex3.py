#a.
def suppEspDeb(ch):
    newCh = ""
    chara = ''
    debut = True
    i = 0
    while i < len(ch) :
        chara = ch[i]
        if chara != ' ':
            debut = False
        if debut == False:
            newCh += chara
        i += 1
    
    return(newCh)

#b.
def suppEspFin(ch): #pas réussi
    return ch.rstrip()

print(suppEspFin("Salut   "), "oui")
