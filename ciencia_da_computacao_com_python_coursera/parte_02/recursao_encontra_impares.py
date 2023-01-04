def encontra_impares(lista):
    lis = []
    if len(lista) > 0:
        numero = lista.pop(0)
        if numero % 2 != 0:
            lis.append(numero)
        lis = lis + encontra_impares(lista)
    return lis


print(encontra_impares([1, 2, 3, 4, 5, 6]))


def encontra_impares_2(lista):
    if len(lista) == 0:
        return []
    e = lista.pop(0)
    if e % 2 != 0:
        return [e] + encontra_impares_2(lista)
    return encontra_impares_2(lista)


print(encontra_impares_2([1, 7, 10, 12, 16, 21, 3, 9, 11]))
