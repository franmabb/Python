frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

contador = 0
for c in frase:
    if c == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces.")
