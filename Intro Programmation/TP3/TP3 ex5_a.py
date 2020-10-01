h = int(input("Heure = "))
m = int(input("Minutes = "))
s = int(input("Secondes = "))

res = (h*3600) + (m*60) + s
print("Il s'est passé", res, "secondes depuis minuit")
