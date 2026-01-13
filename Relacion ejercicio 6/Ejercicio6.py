asignatura = { 'Matematicas'  :  7, 'Fisica' : 4, 'Quimica': 8}
total = 0
for i in asignatura:
    print(f"La asignatura {i}, tiene {asignatura[i]} creditos")
    total +=  asignatura[i]

print(f"El numero total de creditos es {total}")