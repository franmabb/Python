n = int(input("Introduce un número entero positivo: "))
impares = []

for i in range(1, n + 1, 2):
    impares.append(str(i))

print(", ".join(impares))
