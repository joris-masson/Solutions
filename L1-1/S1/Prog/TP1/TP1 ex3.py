taille = float(input("Quelle est votre taille(en m) ? "))
masse = float(input("Quel est votre masse(en kg) ? "))
IMC = masse/(taille**2)

print("Votre IMC est égale à ", IMC, "donc votre classification est: ")

if (IMC < 16.5):
    print("dénutrition ou famine")
elif (IMC <= 16.5) and (IMC < 18.5):
    print("maigreur")
elif (IMC <= 18.5) and (IMC < 25.0):
    print("corpulence normale")
elif (IMC <= 25.0) and (IMC <= 30):
    print("surpoids")
elif (IMC > 30):
    print("obésité")
