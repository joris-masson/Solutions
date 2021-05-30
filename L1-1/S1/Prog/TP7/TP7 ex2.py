val = ()
rep = ""
moy = 0
moyc = 1

while rep != -1:
    rep = int(input("Valeur suivante? -1 pour stopper "))
    moyc += rep
    val += (rep),

moy = moyc/len(val)
print(moy)
