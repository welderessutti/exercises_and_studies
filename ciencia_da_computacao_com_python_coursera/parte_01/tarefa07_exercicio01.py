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
