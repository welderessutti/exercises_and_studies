matriz = [[], [], []]

for c in range(0, 3):
    for x in range(0, 3):
        num = int(input(f'Digite um valor para {[c, x]}: '))
        matriz[c].insert(x, num)

for c in range(0, 3):
    for x in range(0, 3):
        print(f'[{matriz[c][x]: ^5}]', end='')
    print()

# PROFESSOR FEZ ASSIM:

matriz_1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for a in range(0, 3):
    for b in range(0, 3):
        matriz_1[a][b] = int(input(f'Digite um valor para [{a}, {b}]: '))

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz_1[a][b]: ^5}]', end='')
    print()

# UMA FORMA INTELIGENTE QUE POSTARAM:

matriz_2 = []

for x in range(0, 3):
    matriz_2.append([])

    for z in range(0, 3):
        matriz_2[x].append(int(input(f'Digite um valor para [{x}, {z}]: ')))

for linha in matriz_2:
    for num_2 in linha:
        print(f'[{num_2:^5}]', end='')
    print()
