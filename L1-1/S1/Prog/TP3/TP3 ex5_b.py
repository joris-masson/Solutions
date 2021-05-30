h = int(input("Heure = "))
m = int(input("Minutes = "))
s = int(input("Secondes = "))

s += 1

if s>=60:
    s = 00
    m += 1
if m>=60:
    m = 00
    h += 1
if h >= 24:
    h =00

print("Il sera", h, "h", m, "m", s, "s")
