directorio = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

lineas = directorio.split('\n')

campos = lineas[0].split(';')

clientes = {}

for linea in lineas[1:]:
    valores = linea.split(';')
    
    nif = valores[0]
    
    datos_cliente = {}
    
    for campo, valor in zip(campos[1:], valores[1:]):
        if campo == 'descuento':
            datos_cliente[campo] = float(valor)
        else:
            datos_cliente[campo] = valor
            
    clientes[nif] = datos_cliente

for k, v in clientes.items():
    print(f"'{k}': {v}")
