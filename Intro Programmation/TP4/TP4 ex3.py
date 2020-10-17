#1-------------------------------------------------------------------
print("1.")
fruits = ('pomme', 'poire', 'ananas', 'banane', 'citron', 'carambole', 'kiwi')
nombres = ('un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept')

tuples = (fruits, nombres)

leTuple = 0 #tuple à étudier

nbDeMots = 0

for i in range(len(tuples[leTuple])):
    if len(tuples[leTuple][i]) >= 7:
        nbDeMots += 1
print("Dans le tuple choisi, ", nbDeMots, "font plus de 7 caractères \n")

#2-------------------------------------------------------------------
print("2.")
fruits = ('pomme', 'poire', 'ananas', 'banane', 'citron', 'carambole', 'kiwi')
nombres = ('un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept')

tuples = (fruits, nombres)

leTuple = 0 #tuple à étudier

mots = ()

for i in range(len(tuples[leTuple])):
    if tuples[leTuple][i][0] == 'c':
        mots += tuples[leTuple][i]
print(mots, "\n")

#3-------------------------------------------------------------------
print("3.")
fruits = ('pomme', 'poire', 'ananas', 'banane', 'citron', 'carambole', 'kiwi')
nombres = ('un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept')

tuples = (fruits, nombres)

leTuple = 0 #tuple à étudier

motEntre = ''
nbErreurs = 0

for i in range(len(tuples[leTuple])):
    print("Recopie ce mot: ", tuples[leTuple][i])
    motEntre = input()
    if motEntre == tuples[leTuple][i]:
        print("Bravo, au suivant maintenant! \n")
    else:
        print("Ce n'est pas bien recopié, il fallait écrire: ", tuples[leTuple][i])
        nbErreurs += 1
if nbErreurs == 0:
    print("Bravo, tu n'as fait aucune faute!")
elif nbErreurs == 1:
    print("Bravo, tu n'as fait qu'une erreur")
else:
    print("Fait attention, tu as fait: ", nbErreurs, "Erreurs")
