abecedario = [chr(i) for i in range(ord('a'), ord('z')+1)]
resultado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]

print(resultado)
