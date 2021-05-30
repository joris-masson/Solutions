#1
def test(ch, carac):
    if carac in ch:
        return True
    else:
        return False

print(test("oui", "t"))

#2
def saisiePhrase():
    phrase = ''
    for mot in range(100):
        ch = input("Mot ou StopFin pour finir: ")
        if ch == "StopFin":
            return phrase
        else:
            phrase += ch + " "

print(saisiePhrase())

#3
def saisieMot():
    mot = input("mot: ")
    if test(mot, ' '):
        print("Un seul mot")
        return saisieMot()
    else:
        return mot
    
print(saisieMot())

#4
def saisiePhrase2():
    phrase = ''
    for mot in range(100):
        ch = saisieMot()
        if ch == "StopFin":
            return phrase
        else:
            phrase += ch + " "

print(saisiePhrase2())

#5
def saisiePhraseSansE():
    phrase = ''
    for mot in range(100):
        ch = saisieMot()
        if ch == "StopFin":
            return phrase
        elif 'e' in ch:
            return "Perdu"
        else:
            phrase += ch + " "
print(saisiePhraseSansE())

#6
def saisiePhraseSansE_avecCompteur():
    compteur = 0
    
    phrase = ''
    for mot in range(100):
        ch = saisieMot()
        if ch == "StopFin":
            return phrase
        elif 'e' in ch:
            compteur += 1
            print("Il vous reste", abs(compteur-3), "vie(s)")
            if compteur == 3:
                return "Perdu"
        else:
            phrase += ch + " "
            
print(saisiePhraseSansE_avecCompteur())
