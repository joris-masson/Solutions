def massome(n, p):
    res = 0
    
    for i in range(0, n+1):
        res+=i**p
    return res

def main():
    n = int(input("Entier n: "))
    p = int(input("A la puissance: "))

    return massome(n, p)

print(main())
