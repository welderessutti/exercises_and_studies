cont = 0

num = int(input('Digite um número: '))

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[1;34m{c}\033[m', end=' ')
        cont = cont + 1
    else:
        print(f'\033[1;31m{c}\033[m', end=' ')

print(f'\nO número {num} foi divisível {cont} vezes (AZUL).')

if cont == 2:
    print(f'E por isso ele é PRIMO.')
else:
    print('E por isso ele NÃO É PRIMO.')
