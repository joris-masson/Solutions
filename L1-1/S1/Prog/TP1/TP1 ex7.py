from simplification import date

prenom = ""
anneeEnCours = ""
dateDeNaissance = ""

answered = False

while True:
    if answered == False:
        prenom = str(input("Votre prénom: "))
        anneeEnCours = str(input("L'année en cours: "))
        answered = True
    else:
        print("")
        print("Vous êtes", prenom, "et l'année en cours est", anneeEnCours)
    
    dateDeNaissance = str(input("Votre date de naissance(jj/mm/aaaa): "))

    if (len(dateDeNaissance) != 10) or (dateDeNaissance[2] != "/") or (dateDeNaissance[5] != "/"):
        print("Mauvais format de date de naissance")
    else:
        break

jour = dateDeNaissance[0:2]
mois = dateDeNaissance[3:5]
annee = dateDeNaissance[6:10]

dateU = (jour, mois, annee)

age = int(anneeEnCours) - int(dateU[2])

print("Vous vous appelez", prenom, ",vous êtes né(e) en", date.getMonthName(dateU[1]), dateU[2], " et vous avez", age, "ans(si c'est faux, vous pouvez me taper)")
