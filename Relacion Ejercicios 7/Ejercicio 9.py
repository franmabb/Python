def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return (a * b) // mcd(a, b)

print(mcd(24, 36))
print(mcm(24, 36))