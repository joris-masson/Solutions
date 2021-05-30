desMots1 = ["ohhhhh", "tartiflette", "raclette", "gouda", "jambon", "saucisson"]
desMots2 = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit"]

def modifie(ch):
    listeChara = list(ch)
    for lettre in range(len(ch)):
        if ch[lettre] == 'a':
            listeChara[lettre] = '@'
    return ''.join(listeChara)

def modifieListe(l):
    """
    #Version for "normale"
    
    newL = []
    for elem in l:
       newL.append(modifie(elem))
    return newL
    """
    return [modifie(elem) for elem in l]

print(modifieListe(desMots1))
