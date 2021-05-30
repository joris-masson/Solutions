def maximum(a, b):
    return max(a, b)

def maximum4(a, b, c, d):
    plusGrand1 = maximum(a,b)
    plusGrand2 = maximum(c,d)
    return maximum(plusGrand1, plusGrand2)

print(maximum(12,1))
print(maximum4(15,3,17,15))
