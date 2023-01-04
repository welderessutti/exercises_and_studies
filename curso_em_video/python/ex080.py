lista = []

for c in range(0, 5):
    num = int(input('Digite um valor: '))

    if c == 0:
        lista.append(num)
        print(f'Adiconado na posição {lista.index(num)}')

    elif num >= max(lista):
        lista.insert(len(lista), num)
        print(f'Adicionado na posição {lista.index(num)} da lista...')

    elif min(lista) <= num <= max(lista):
        for d, e in enumerate(lista):
            if num <= e:
                lista.insert(d, num)
                print(f'Adicionado na posição {lista.index(num)} da lista...')
                break

    elif num <= min(lista):
        lista.insert(- len(lista), num)
        print(f'Adicionado na posição {lista.index(num)} da lista...')

print(lista)

# PROFESSOR FEZ ASSIM (MUITO MELHOR):

lista_1 = []

for w in range(0, 5):
    num = int(input('Digite um valor: '))

    if w == 0 or num > lista_1[-1]:
        lista_1.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0  # CONTADOR DE POSIÇÕES DA LISTA
        while pos < len(lista_1):
            if num <= lista_1[pos]:
                lista_1.insert(pos, num)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1

print(lista_1)
