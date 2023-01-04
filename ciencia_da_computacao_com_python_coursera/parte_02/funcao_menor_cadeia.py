def menor_cadeia(lista):
    menor = lista[0].strip()
    for a in lista:
        if len(a.strip()) < len(menor.strip()):
            menor = a.strip()
    return menor.capitalize()


print(menor_cadeia(['Bárbara', 'JOSÉ  ', 'Bill']))
