n = int(input("Introduce un número entero: "))

for i in range(1, n + 1):
    fila = []
    for j in range(i):
        fila.append(str(2*i - 1 - 2*j))
    print(" ".join(fila))
