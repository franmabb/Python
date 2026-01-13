meses = {
    '01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril',
    '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto',
    '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
}

fecha = input("Introduce una fecha (dd/mm/aaaa): ")
partes = fecha.split('/')

if len(partes) == 3 and partes[1] in meses:
    dia = partes[0]
    mes = meses[partes[1]]
    anio = partes[2]
    print(f"{dia} de {mes} de {anio}")
else:
    print("Formato de fecha incorrecto o mes no válido.")
