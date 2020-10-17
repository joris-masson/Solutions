"""
Bibliothèque visant à simplifier le code vis-à-vis des dates. J'ai fait en sorte de marquer les 
entrées/sorties pour que ce soit plus simple.
(Créé pour les TP de prog)
"""

#Entrée: mois -> str
#Sortie: str
def getMonthName(mois):
    if mois == "01":
        return "janvier"
    elif mois == "02":
        return "février"
    elif mois == "03":
        return "mars"
    elif mois == "04":
        return "avril"
    elif mois == "05":
        return "mai"
    elif mois == "06":
        return "juin"
    elif mois == "07":
        return "juillet"
    elif mois == "08":
        return "août"
    elif mois == "09":
        return "septembre"
    elif mois == "10":
        return "octobre"
    elif mois == "11":
        return "novembre"
    elif mois == "12":
        return "décembre"
    else:
        print("Valeure incorrecte")

#Entrées: month -> str ; year -> int
#Sortie: int
def getNbDeJours(month, year):
    mois31 = ('01', '03', '05', '07', '08', '10', '12')
    if month in mois31:
        return 31
    elif month == '02':
        if (((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)): #année bissextile
            return 29
        else: #non bissextile
            return 28
    else:
        return 30

#Entrée: num -> int
#Sortie: str
def convertMonth(num):
    if num < 10:
        return ('0' + str(num))
    else:
        return (str(num))

#Entrée: date -> tuple(jj, mm, aaaa)
#Sortie: demain -> tuple(jj, mm, aaaa)
def getNextDay(date):
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    day = day + 1
    
    if day > getNbDeJours(convertMonth(month), year):
        month = month + 1
        day = 1

    if month > 12:
        year = year + 1
        month = 1
    
    demain = (day, convertMonth(month), year)
    return demain


#Entrée: date -> tuple(jj, mm, aaaa)
#Sortie: newFormat -> str
def changeFormat(date):
    day = str(date[0])
    month = str(date[1])
    year = str(date[2])

    newFormat = day + "/" + month + "/" + year
    return newFormat
