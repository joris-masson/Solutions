entier = int(input("Entrez un entier: "))
res = entier

for i in range(1, entier):
    print("le nombre qui suit", i, "est", i+1) 
    res+=i
print("La somme des entiers de 1 à", entier, "est:", res)
