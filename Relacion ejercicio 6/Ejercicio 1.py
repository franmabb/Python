divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa = input("Introduce el nombre de una divisa: ")

if divisa in divisas:
    print(f"El símbolo de {divisa} es {divisas[divisa]}")
else:
    print("La divisa no está en el diccionario.")
