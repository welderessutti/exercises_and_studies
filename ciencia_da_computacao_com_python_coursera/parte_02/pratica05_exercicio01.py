def insertion_sort(lista):
    for a in range(len(lista) - 1):
        for b in range(a + 1, len(lista)):
            if lista[a] > lista[b]:
                x = lista[a]
                lista[a] = lista[b]
                lista[b] = x
    return lista
