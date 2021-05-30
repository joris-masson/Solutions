#a
def somChaine(ch):
    somme = 0
    for chiffre in ch:
        somme += int(chiffre)
    return somme

#b
def test(ch):
    s = somChaine(ch)
    if s %3 == 0:
        return True
    else:
        return False
print(test("46374623698265982659263598639856928365"))
