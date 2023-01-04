def maiusculas(frase):  # AQUI EU USEI O "ISUPPER":
    pos = 0
    letras_maiusculas = ""
    while pos < len(frase):
        if frase[pos].isupper():
            letras_maiusculas += frase[pos]
        pos += 1
    return letras_maiusculas


def maiusculas_2(frase):  # AQUI EU GEREI UMA LISTA COM OS CÓDIGOS DECIMAIS (ORD):
    lista_dec = list(range(65, 91))
    pos = 0
    letras_maiusculas = ""
    while pos < len(frase):
        if ord(frase[pos]) in lista_dec:
            letras_maiusculas += frase[pos]
        pos += 1
    return letras_maiusculas
