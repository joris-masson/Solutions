age = int(input("Quel est votre âge? "))
sexe = input("Quel est votre sexe? (h/f) ")

if (sexe == 'h') and (age >= 20):
    print("Vous payez l'impôt")
elif (sexe == 'f') and ((age >= 18) and (age <= 35)):
    print("vous payer l'impôt")
else:
    print("Vous ne payez pas l'impôt")
