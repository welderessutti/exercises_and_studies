def primeiro_lex(lista):
    menor = lista[0]
    for a in lista:
        if a < menor:
            menor = a
    return menor
