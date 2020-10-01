"""
Bibliothèque visant à simplifier le code vis-à-vis des dates.
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
    if month == '01': #janvier
        return 31
    elif month == '02': #février
        if (((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)): #année bissextile
            return 29
        else: #non bissextile
            return 28
    elif month == '03': #mars
        return 31
    elif month == '04': #avril
        return 30
    elif month == '05': #mai
        return 31
    elif month == '06': #juin
        return 30
    elif month == '07': #juillet
        return 31
    elif month == '08': #août
        return 31
    elif month == '09': #septembre
        return 30
    elif month == '10': #octobre
        return 31
    elif month == '11': #novembre
        return 30
    elif month == '12': #décembre
        return 31

#Entrée: num -> int
#Sortie: str
def convertMonth(num):
    if num == 1:
        return '01'
    elif num == 2:
        return '02'
    elif num == 3:
        return '03'
    elif num == 4:
        return '04'
    elif num == 5:
        return '05'
    elif num == 6:
        return '06'
    elif num == 7:
        return '07'
    elif num == 8:
        return '08'
    elif num == 9:
        return '09'
    elif num == 10:
        return '10'
    elif num == 11:
        return '11'
    elif num == 12:
        return '12'
    else:
        return '00'

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
    
    demain = (day, month, year)
    return demain
