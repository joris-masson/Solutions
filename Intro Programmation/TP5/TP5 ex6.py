def Zuckerman(nb):
    leNb = str(nb)
    res = 0
    if '0' in leNb:
        return False
    else:
        for nombre in range(len(leNb)):
            res += nb%int(leNb[nombre])
        if res == 0:
            return True
        else:
            return False

def afficheZuckerman(debut, fin):
    for nb in range(debut, fin):
        if Zuckerman(nb):
            print(nb)
afficheZuckerman(10, 100)
