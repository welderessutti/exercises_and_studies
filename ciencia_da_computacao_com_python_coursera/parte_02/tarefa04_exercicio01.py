def ordenada(lista):
    fim = len(lista)
    for i in range(fim - 1):
        menor_posicao = i
        for j in range(i + 1, fim):
            if lista[j] < lista[menor_posicao]:
                return False
    return True
