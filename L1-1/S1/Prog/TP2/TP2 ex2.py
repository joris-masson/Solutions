REF = -10**25

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

plusGrand = REF

if (plusGrand > a) and (plusGrand > b) and (plusGrand > c):
    print("Les trois nombres sont trop petit par rapport au nombre de référence: ", REF)
    exit()
    
liste = [a, b, c]

for i in range(len(liste)):
    if liste[i] >= plusGrand:
        plusGrand = liste[i]

print(plusGrand)
