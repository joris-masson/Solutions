#1.------------------------------------
res = 0

for i in range(0,64):
    res+= 2**i
print(res)

#2.------------------------------------
res = 0
tupleEntier = (10, 3, 6, 7)
for i in range(len(tupleEntier)):
    res+=tupleEntier[i]
print(res)
