def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_frecuente(diccionario):
    palabra_max = ""
    cantidad_max = 0
    for palabra, cantidad in diccionario.items():
        if cantidad > cantidad_max:
            palabra_max = palabra
            cantidad_max = cantidad
    return (palabra_max, cantidad_max)

texto = "hola python hola mundo python python"
diccionario_generado = contar_palabras(texto)

print(diccionario_generado)
print(palabra_mas_frecuente(diccionario_generado))