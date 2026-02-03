def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in binario[::-1]:
        decimal += int(digito) * 2 ** potencia
        potencia += 1
    return decimal

print(decimal_a_binario(20))
print(binario_a_decimal("10100"))