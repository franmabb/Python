facturas = {}
cobrado = 0

while True:
    opcion = input("¿Añadir, Pagar o Terminar? ").lower()
    if opcion == "añadir":
        num = input("Número de factura: ")
        coste = float(input("Coste: "))
        facturas[num] = coste
    elif opcion == "pagar":
        num = input("Número de factura a pagar: ")
        if num in facturas:
            cobrado += facturas.pop(num)
        else:
            print("Factura no encontrada.")
    elif opcion == "terminar":
        break
    print(f"Cobrado: {cobrado:.2f}")
    print(f"Pendiente: {sum(facturas.values()):.2f}")