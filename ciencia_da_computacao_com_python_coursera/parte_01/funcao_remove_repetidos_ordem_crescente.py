def remove_repetidos(lista):
    nova_lista = []
    for a in lista:
        if a not in nova_lista:
            nova_lista.append(a)
    for b in range(len(nova_lista) - 1):
        for c in range(b + 1, len(nova_lista)):
            if nova_lista[b] > nova_lista[c]:
                x = nova_lista[b]
                nova_lista[b] = nova_lista[c]
                nova_lista[c] = x
    lista = nova_lista[:]
    return lista


lala = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lala = remove_repetidos(lala)

print(lala)
