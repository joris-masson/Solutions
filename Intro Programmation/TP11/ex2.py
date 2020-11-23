from simplification import grille

ex = [ ['P','Y','T','H','O','N'] , ['R','*','A','U','M','A'], ['O','M','B','R','E','*'], ['G','A','L','E','T','S'], ['*','T','E','*','S','U']]

grille.afficheGrille(ex)

def uneLettre(maGrille):
    for ligne in maGrille:
        for elem in ligne:
            if len(elem) > 1:
                return False
    return True

def prendLigne(maGrille, ligne):
    return str(maGrille[ligne])

print(prendLigne(ex, 3))
