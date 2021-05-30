from simplification import date

date_ = input("Veuillez entrer une date sous la forme jj/mm/aaaa: ")

if (len(date_) != 10) or (date_[2] != "/") or (date_[5] != "/"):
        print("Mauvais format de date de naissance")

jour = date_[0:2]
mois = date_[3:5]
annee = date_[6:10]

tupleDate = (jour, mois, annee)

print(date.changeFormat(date.getNextDay(tupleDate)))
