#1------------------------------------------
print("1.")
ch = "coucou"
res = ""

for char in ch:
    res += char*2
print(res, "\n")

#2------------------------------------------
print("2.")
ch = "j'aime beaucoup la vie vous pouvez me croire"
res = ""
temp = 0

for char in ch:
    if temp %2 == 0:
        res += char
    else:
        res += "*"
    temp += 1
print(res, "\n")

#3------------------------------------------
voyelles = ('a', 'e', 'i', 'o', 'u')
ch = "Bonjour vous"
nbVoyelles = 0
nbEspaces = 0
for char in ch:
    if char in voyelles:
        nbVoyelles += 1
    if char == " ":
        nbEspaces += 1
print("Il y a ", nbVoyelles, "voyelles, et ", nbEspaces, "Espaces")
