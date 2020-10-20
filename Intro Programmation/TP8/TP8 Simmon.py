import random

def saut(n):
    print("\n" * n)

def alea():
    return str(random.randint(0,2))

def affiche(ch):
    for lettre in ch:
        print(lettre, end=' ')
    print("\n")
    
def sansEspaces(ch):
    return ch.replace(' ', '')

def simmon():
    rep = ''
    nums = ''
    score = 0
    while True:
        nums += alea()
        affiche(nums)
        input("Appuyez sur 'entrée' une fois mémorisée")
        saut(50)
        rep = sansEspaces(input("La suite est: "))
        if rep == nums:
            print("Bravo, plus dur maintenant")
            score += 1
        else:
            print("GG, vous avez perdu, vous score est de: ", score)
            return score

def Continue():
    rep = ""
    while ((rep != "Oui") and (rep != "Non")):
        rep = input("Voulez-vous continuer?(Oui ou Non) ")
    if rep == "Oui":
        return True
    else:
        return False

def main():
    meilleurScore = 0
    continuer = True
    while continuer != False:
        scoreAct = simmon()
        if scoreAct > meilleurScore:
            meilleurScore = scoreAct
        print("Votre meilleur score est de: ", meilleurScore)
        continuer = Continue()
        
main()
