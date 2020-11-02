COULEURS = ('n', 'b', 'v', 'r')
HAUTEURS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

cartes = []

def couple(l1, l2):
    return [[x, y] for x in l1 for y in l2]

def creation():
    jeu = couple(COULEURS, HAUTEURS)*2
    for i in range(2):
        jeu.append(["j", "j"])
    return jeu

cartes = creation()
print(cartes)
print(len(cartes))
