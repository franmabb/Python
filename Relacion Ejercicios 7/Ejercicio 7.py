def calcular_cuadrados(lista):
    cuadrados = []
    for numero in lista:
        cuadrados.append(numero ** 2)
    return cuadrados

print(calcular_cuadrados([1, 2, 3, 4, 5]))