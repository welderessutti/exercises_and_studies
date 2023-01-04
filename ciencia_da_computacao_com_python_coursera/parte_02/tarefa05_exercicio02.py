def bubble_sort(lista):
    for a in range(len(lista) - 1, 0, -1):
        trocou = False
        for b in range(a):
            if lista[b] > lista[b + 1]:
                lista[b], lista[b + 1] = lista[b + 1], lista[b]
                print(lista)
                trocou = True
        if not trocou:
            return lista
    return lista
