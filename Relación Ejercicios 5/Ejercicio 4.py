numeros = []

print("Introduce los 6 números ganadores de la lotería primitiva:")

for i in range(6):
    numero = int(input(f"Número {i+1}: "))
    numeros.append(numero)

numeros.sort()  # Ordenar de menor a mayor

print("Los números ganadores ordenados son:")
print(numeros)
