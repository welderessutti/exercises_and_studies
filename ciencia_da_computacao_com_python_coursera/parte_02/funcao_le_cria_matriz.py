def cria_matriz(lin, col):
    matriz = []
    for a in range(lin):
        linha = []
        for b in range(col):
            valor = int(input(f"Digite o valor da posição [{a}][{b}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def le_matriz():
    linha = int(input("Matriz com quantas linhas?: "))
    coluna = int(input("Matriz com quantas colunas?: "))
    matriz = cria_matriz(linha, coluna)
    for a in matriz:
        for b in a:
            print(f"{b:^3}", end=" ")
        print()


le_matriz()
