cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual (en %): ")) / 100
años = int(input("Número de años: "))

for i in range(1, años + 1):
    cantidad *= (1 + interes)
    print(f"Año {i}: {cantidad:.2f} €")
