
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu teléfono? ")

datos = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es {datos['telefono']}.")