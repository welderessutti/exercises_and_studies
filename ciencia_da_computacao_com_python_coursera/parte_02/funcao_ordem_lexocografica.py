def primeiro_lex(lista):
    menor = lista[0].capitalize()
    for a in lista:
        if a.capitalize() < menor.capitalize():
            menor = a.capitalize()
    return menor


bla = ["ana", "maria", "José", "Valdemar"]

print(primeiro_lex(bla))
