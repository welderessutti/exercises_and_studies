def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito
    if not lado_direito:
        return lado_esquerdo
    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


abc = [5, 2, 7, 9, 3, 4, 6, 1, 2, 3, 0]

print(merge_sort(abc))
