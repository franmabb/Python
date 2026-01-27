Datos = {}

while True:
    print("\n1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nif = input("NIF: ")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        pref = input("¿Cliente preferente? (s/n): ").lower() == "s"
        Datos[nif] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": pref
        }
    elif opcion == "2":
        nif = input("NIF del cliente a eliminar: ")
        Datos.pop(nif, None)
    elif opcion == "3":
        nif = input("NIF del cliente a mostrar: ")
        cliente = Datos.get(nif)
        if cliente:
            print(cliente)
        else:
            print("Cliente no encontrado.")
    elif opcion == "4":
        for nif, cliente in Datos.items():
            print(nif, cliente["nombre"])
    elif opcion == "5":
        for nif, cliente in Datos.items():
            if cliente["preferente"]:
                print(nif, cliente["nombre"])
    elif opcion == "6":
        break