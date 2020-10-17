def saisieON():
    rep = ""
    while ((rep != "OUI") and (rep != "NON")):
        rep = input("OUI ou NON: ")
    if rep == "OUI":
        return 1
    else:
        return 0
print(saisieON())
print("lol")
