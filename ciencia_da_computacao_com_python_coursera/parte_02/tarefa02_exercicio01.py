def maiusculas(frase):
    lista_dec = list(range(65, 91))
    pos = 0
    letras_maiusculas = ""
    while pos < len(frase):
        if ord(frase[pos]) in lista_dec:
            letras_maiusculas += frase[pos]
        pos += 1
    return letras_maiusculas
