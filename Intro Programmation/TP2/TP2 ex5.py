from simplification import date

nom = input("Votre nom: ")
departement = input("Votre département de naissance: ")
dateDeNaissance = input("Veuillez entrer votre date de naissance sous la forme jj/mm/aaaa: ")

identifiant = ''

if (len(dateDeNaissance) != 10) or (dateDeNaissance[2] != "/") or (dateDeNaissance[5] != "/"):
        print("Mauvais format de date de naissance")

jour = dateDeNaissance[0:2]
mois = dateDeNaissance[3:5]
annee = dateDeNaissance[6:10]

print("Bonjour M./Mme", nom, "vous êtes né(e) en", date.getMonthName(mois), annee, "Votre département est:", departement, "et vous avez", (2020-int(annee)), "ans")

if len(nom) < 3:
    identifiant = annee[:2] + nom + "*" + departement + annee
else:
    identifiant = annee[:2] + nom[:3] + departement + annee

print("Votre identifiant est: ", identifiant)
