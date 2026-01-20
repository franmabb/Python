cesta = {}

while True:
    articulo = input("Introduce el nombre del artículo (o 'fin' para terminar): ")
    if articulo.lower() == 'fin':
        break
    try:
        precio = float(input(f"Introduce el precio de '{articulo}': "))
        cesta[articulo] = precio
    except ValueError:
        print("Por favor, introduce un precio válido.")

print("\nLista de la compra")
total = 0
for articulo, precio in cesta.items():
    print(f"{articulo}: {precio:.2f} €")
    total += precio
print(f"Total: {total:.2f} €")