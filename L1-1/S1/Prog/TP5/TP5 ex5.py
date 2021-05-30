def retourne(ch):
    newCh = ''
    newCh = ch[::-1]
    return newCh

def test_palin(mot):
    if mot == retourne(mot):
        return 1
    else:
        return 0

    testCh = ''
    testCh = mot[::-1]
    if testCh == mot:
        return 1
    else:
        return 0
    #La plus efficace est avec la f() retourne
    
def anneePalin(n):
    test = 0
    for annee in range(n):
        test = test_palin(str(annee))
        if test == 1:
            print(annee)
print(anneePalin(5000))
