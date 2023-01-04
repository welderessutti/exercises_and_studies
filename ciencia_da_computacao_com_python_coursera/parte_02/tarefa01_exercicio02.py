def dimensoes(matriz):
    return len(matriz), len(matriz[0])


def soma_matrizes(m1, m2):
    dim_m1 = dimensoes(m1)
    dim_m2 = dimensoes(m2)
    if dim_m1 == dim_m2:
        matriz = []
        for a in range(dim_m1[0]):
            linha = []
            for b in range(dim_m1[1]):
                linha.append(m1[a][b] + m2[a][b])
            matriz.append(linha)
        return matriz
    else:
        return False
