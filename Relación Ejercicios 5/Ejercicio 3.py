asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas.append(nota)

for asignatura, nota in zip(asignaturas, notas):
    print(f"En {asignatura} has sacado {nota}")

