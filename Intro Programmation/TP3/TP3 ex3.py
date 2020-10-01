nbDeNotes = int(input("Nombre de notes à renter: "))
notes = []
aDire = ''
moy = 0
moyc = 0
for i in range(nbDeNotes):
    aDire = "Note " + str(i+1) + ' '
    notes.append(float(input(aDire)))

for i in range(len(notes)):
    moyc += notes[i]
moy = moyc/len(notes)
print(moy)
