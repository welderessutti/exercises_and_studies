matriz = [[], [], []]
soma_par = soma_coluna3 = maior = 0

for a in range(0, 3):
    for b in range(0, 3):
        num = int(input(f'Digite um valor para [{a}, {b}]: '))
        matriz[a].insert(b, num)

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]: ^5}]', end='')
        if matriz[a][b] % 2 == 0:
            soma_par += matriz[a][b]
        if b == 2:
            soma_coluna3 += matriz[a][b]
        if a == 1 and b == 0:
            maior = matriz[a][b]
        elif a == 1 and b != 0:
            if matriz[a][b] > maior:
                maior = matriz[a][b]
    print()

print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}.')
print(f'O maior valor da segunda linha é {maior}.')

# UMA FORMA INTELIGENTE QUE POSTARAM:

matriz_1 = []
soma_par2 = soma_coluna3_2 = maior_2 = 0

for c in range(0, 3):
    matriz_1.append([])

    for d in range(0, 3):
        matriz_1[c].append(int(input(f'Digite um valor para [{c}, {d}]: ')))

for linha, e in enumerate(matriz_1):
    for flag, f in enumerate(e):
        print(f'[{f:^5}]', end='')
        if f % 2 == 0:
            soma_par2 += f
        if flag == 2:
            soma_coluna3_2 += f
        if linha == 1 and flag == 0:
            maior_2 = f
        elif linha == 1 and flag != 0:
            if f > maior_2:
                maior_2 = f
    print()

print(f'A soma dos valores pares é {soma_par2}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna3_2}.')
print(f'O maior valor da segunda linha é {maior_2}.')
