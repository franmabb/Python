def area_circulo(radio):
    return 3.1416 * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

r = float(input("Introduce el radio del círculo/cilindro: "))
h = float(input("Introduce la altura del cilindro: "))
print("Área del círculo:", area_circulo(r))
print("Volumen del cilindro:", volumen_cilindro(r, h))