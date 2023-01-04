import random
from time import sleep
# Gerador de jogos com range do "randint":
lista = []

jogos = int(input('Quantos jogos você quer que eu sorteie?: '))

for c in range(0, jogos):
    lista.append([])
    cont = 0

    while cont < 6:
        sorteado = random.randint(1, 60)
        if sorteado not in lista[c]:
            lista[c].append(sorteado)
            cont += 1

    lista[c].sort()
    sleep(1)

    print(f'Jogo {c + 1}: {sorted(lista[c])}')

# PROFESSOR FEZ UM POUCO DIFERENTE, MAS NÃO COPIEI AQUI AINDA...

# Alterador de ordem dos números da lista:
ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

inicio = 0
fim = -1
for x in range(len(ordenada) // 4):
    ordenada[inicio], ordenada[fim] = ordenada[fim], ordenada[inicio]
    inicio += 2
    fim -= 2

print(ordenada)

# Gerador de jogos com as minhas listas:
abc = [1, 59, 3, 57, 5, 55, 7, 53, 9, 51, 11, 49, 13, 47, 15, 45, 17, 43, 19, 41, 21, 39, 23, 37, 25, 35, 27, 33, 29, 31, 30, 32, 28, 34, 26, 36, 24, 38, 22, 40, 20, 42, 18, 44, 16, 46, 14, 48, 12, 50, 10, 52, 8, 54, 6, 56, 4, 58, 2, 60]
xyz = [60, 2, 58, 4, 56, 6, 54, 8, 52, 10, 50, 12, 48, 14, 46, 16, 44, 18, 42, 20, 40, 22, 38, 24, 36, 26, 34, 28, 32, 30, 31, 29, 33, 27, 35, 25, 37, 23, 39, 21, 41, 19, 43, 17, 45, 15, 47, 13, 49, 11, 51, 9, 53, 7, 55, 5, 57, 3, 59, 1]
www = [1, 59, 3, 57, 5, 55, 7, 53, 9, 51, 11, 49, 13, 47, 15, 45, 17, 43, 19, 41, 21, 39, 23, 37, 25, 35, 27, 33, 29, 31, 30, 32, 28, 34, 26, 36, 24, 38, 22, 40, 20, 42, 18, 44, 16, 46, 14, 48, 12, 50, 10, 52, 8, 54, 6, 56, 4, 58, 2, 60, 60, 2, 58, 4, 56, 6, 54, 8, 52, 10, 50, 12, 48, 14, 46, 16, 44, 18, 42, 20, 40, 22, 38, 24, 36, 26, 34, 28, 32, 30, 31, 29, 33, 27, 35, 25, 37, 23, 39, 21, 41, 19, 43, 17, 45, 15, 47, 13, 49, 11, 51, 9, 53, 7, 55, 5, 57, 3, 59, 1]

lista_2 = []

jogos = int(input('Quantos jogos você quer que eu sorteie?: '))

for c in range(0, jogos):
    lista_2.append([])
    cont = 0

    while cont < 3:
        while True:
            sorteado = random.choice(abc)
            if sorteado not in lista_2[c]:
                lista_2[c].append(sorteado)
                break
        while True:
            sorteado_2 = random.choice(xyz)
            if sorteado_2 not in lista_2[c]:
                lista_2[c].append(sorteado_2)
                break
        cont += 1

    lista_2[c].sort()
    sleep(1)

    print(f'Jogo {c + 1}: {sorted(lista_2[c])}')
