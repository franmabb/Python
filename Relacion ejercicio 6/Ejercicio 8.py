def construir_diccionario(entrada):
    d = {}
    for par in entrada.split(','):
        par = par.strip()
        if not par:
            continue
        if ':' in par:
            clave, tradu = par.split(':', 1)
            d[clave.strip().lower()] = tradu.strip()
    return d

def traducir_frase(frase, dic):
    puntuacion = '.,;:!?()[]{}"\''
    palabras = frase.split()
    resultado = []
    for tok in palabras:
        original = tok

        pref = ''
        while tok and tok[0] in puntuacion:
            pref += tok[0]
            tok = tok[1:]
        suf = ''
        while tok and tok[-1] in puntuacion:
            suf = tok[-1] + suf
            tok = tok[:-1]
        if not tok:
            resultado.append(original)
            continue
        clave = tok.lower()
        trad = dic.get(clave, tok)
        if tok[0].isupper():
            trad = trad.capitalize()
        resultado.append(f"{pref}{trad}{suf}")
    return ' '.join(resultado)

if __name__ == "__main__":
    entrada = input("Introduce pares palabra:traducción separados por comas:\n")
    dic = construir_diccionario(entrada)
    frase = input("Introduce una frase en español a traducir:\n")
    print("Traducción:")
    print(traducir_frase(frase, dic))