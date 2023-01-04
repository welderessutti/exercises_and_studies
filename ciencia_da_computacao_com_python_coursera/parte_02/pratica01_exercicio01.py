def imprime_matriz(matriz):
    for a in range(len(matriz)):
        for b in range(len(matriz[0])):
            if b != len(matriz[0]) - 1:
                print(matriz[a][b], end=" ")
            else:
                print(matriz[a][b])
