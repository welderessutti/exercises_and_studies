def ordena(lista):
    fim = len(lista)
    for i in range(fim - 1):
        posicao_menor = i
        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_menor]:
                posicao_menor = j
        lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]
    return lista
