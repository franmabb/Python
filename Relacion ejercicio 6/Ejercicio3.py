precios = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

fruta = input("Introduce una fruta: ")
kilos = input("Introduce el número de kilos: ")

try:
    kilos = float(kilos)
except ValueError:
    print("Por favor, introduce un número válido de kilos.")
    exit()

if fruta in precios:
    total = precios[fruta] * kilos
    print(f"{kilos} kilos de {fruta} cuestan {total:.2f} euros.")
else:
    print("La fruta no está en el diccionario.")
