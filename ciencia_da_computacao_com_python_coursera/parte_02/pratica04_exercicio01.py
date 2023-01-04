def lista_grande(n):
    from random import randint
    lista = list()
    for i in range(n):
        lista.append(randint(0, 999))
    return lista
