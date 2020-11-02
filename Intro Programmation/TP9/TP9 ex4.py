liste1 = [0, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 0]
liste2 = ["a", "b", "c", "d"]
liste3 = ["a", "b", "d", "c"]
liste4 = [0, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 0]

desMots1 = ["ohhhhh", "tartiflette", "raclette", "gouda", "jambon", "saucisson"]
desMots2 = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit"]

carac = ['*', '@', '-', '_', '#', '&']

def pairs(l):
    return [i for i in l if i%2 == 0]

def posZero(l):
    return [i for i in range(len(l)) if l[i]==0]


def listeDivi(n):
    return [divi for divi in range(n) if n%divi == 0]
print(listeDivi(30))

def somme(l1, l2):
    return [l1[i]+l2[i] for i in range(len(l1))]

def extrait(c, l):
    return [mot for mot in l if c in mot]

def couple(l1, l2):
    return [[x, y] for x in l1 for y in l2]

print(couple(liste1, carac))
