def estadisticas(lista):
    media = sum(lista) / len(lista)

    suma_diferencias = 0
    for numero in lista:
        suma_diferencias += (numero - media) ** 2
    varianza = suma_diferencias / len(lista)

    desviacion = varianza ** 0.5
    
    return {"media": media, "varianza": varianza, "desviacion": desviacion}

print(estadisticas([10, 20, 30, 40, 50]))