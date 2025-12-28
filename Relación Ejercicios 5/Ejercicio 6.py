
asignaturas = ["Matematicas", "Fisica", "Lengua", "TIC", "Historia"]
asignaturas_repetir = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota < 5:
        asignaturas_repetir.append(asignatura)

print("Tienes que repetir las siguientes asignaturas:")
for asignatura in asignaturas_repetir:
    print(asignatura)

