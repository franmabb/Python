n = int(input("Introduce un número entero positivo: "))
cuenta = []

for i in range(n, -1, -1):
    cuenta.append(str(i))

print(", ".join(cuenta))
