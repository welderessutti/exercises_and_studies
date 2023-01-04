a = []

for b in range(0, 5):
    a.append(int(input(f'Digite um valor para a posição {b}: ')))

print(f'Você digitou os valores {a}.')

print(f'O maior valor digitado foi {max(a)} nas posições ', end='')
for c, d in enumerate(a):
    if d == max(a):
        print(c, end='... ')

print(f'\nO menor valor digitado foi {min(a)} nas posições ', end='')
for e, f in enumerate(a):
    if f == min(a):
        print(e, end='... ')

# PROFESSOR FEZ DESSA FORMA:

print('\n')

listanum = []
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print(f'Você digitou os valores {listanum}.')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
