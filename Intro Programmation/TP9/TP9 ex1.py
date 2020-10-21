liste1 = [0, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 0]
liste2 = ["a", "b", "c", "d"]
liste3 = ["a", "b", "d", "c"]

def tousZero(l):
    if sum(l) == 0:
        return True
    else:
        return False

def auMoinsZero(l):
    if 0 in l:
        return True
    else:
        return False

def compte(x, l):
    cp = 0
    for elem in l:
        if elem == x:
            cp += 1
    return cp

def pairs(l):
    return [i for i in l if i%2 == 0]

def posZero(l):
    index = []
    for i in range(len(l)):
        if l[i] == 0:
            index.append(i)
    return index

def suppDouble(l):
    newL = []
    for elem in l:
        if elem not in newL:
            newL.append(elem)
    return newL

def testAlpha(l):
    listeTest = sorted(l)
    if l == listeTest:
        return True
    else:
        for elem in range(len(l)):
            if l[elem] != listeTest[elem]:
                return l[elem]
print(testAlpha(liste3))
