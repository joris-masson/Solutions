voyelles = ('a', 'e', 'i' ,'o' ,'u', 'y')
ch = input("Entrez quelque chose: ")
newCh = ''

for lettre in ch:
    if lettre in voyelles:
        newCh += '*'
    elif lettre == ' ':
        newCh += '_'
    else:
        newCh += lettre
print(newCh)
