def maior_elemento(lista):
    maior = 0
    for a in range(len(lista)):
        if a == 0:
            maior = lista[a]
        else:
            if lista[a] > maior:
                maior = lista[a]
    return maior
