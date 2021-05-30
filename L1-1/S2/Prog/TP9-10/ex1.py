a = [4, '+', 6]
b = [[7, '-', 2], '*', 5]
c = [[7, '*', [2, '*', 4]], '*', [4, '*', 3]]
d = [[7, '*', [2, '*', [8, '-', 4]]], '-', [11, '+', 5]]
cMoche = [[7, '*', [2, '$', 4]], '*', [4, '$', 3]]

def element(e):
    return type(e) != list

def arg1(e):
    return e[0]
def arg2(e):
    return e[2]
def op(e):
    return e[1]

def creeExp(a1, op, a2):
    return [a1, op, a2]

def comptePlus(e):
    if element(e):
        return 0
    elif op(e) == '+':
        return 1 + comptePlus(arg1(e)) + comptePlus(arg2(e))
    else:
        return comptePlus(arg1(e)) + comptePlus(arg2(e))

def isOnlyMult(e):
    if element(e):
        return True
    elif op(e) != '*':
        return False
    else:
        return isOnlyMult(arg1) and isOnlyMult(arg2)

def calcul(e):
    if element(e):
        return e
    elif op(e) == '+':
        return calcul(arg1(e)) + calcul(arg2(e))
    elif op(e) == '-':
        return calcul(arg1(e)) - calcul(arg2(e))
    elif op(e) == '*':
        return calcul(arg1(e)) * calcul(arg2(e))
    elif op(e) == '/':
        return calcul(arg1(e)) / calcul(arg2(e))
    else:
        return calcul(arg1(e)) + calcul(arg2(e))

def remplace(e):
    if element(e):
        return e
    elif op(e) == '$':
        return creeExp(remplace(arg1(e)), '*', remplace(arg2(e)))
    else:
        return creeExp(remplace(arg1(e)), op(e), remplace(arg2(e)))

print(comptePlus(d))
print(isOnlyMult(c))
print(calcul(d))
print(remplace(cMoche))
