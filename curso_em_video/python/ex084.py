a = []
b = []
maior = menor = 0

while True:
    a.append(input('Nome: '))
    a.append(float(input('Peso: ')))
    if len(b) == 0:
        maior = menor = a[1]
    else:
        if a[1] > maior:
            maior = a[1]
        if a[1] < menor:
            menor = a[1]

    b.append(a[:])
    a.clear()

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print(f'Ao todo, você cadastrou {len(b)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for x in b:
    if x[1] == maior:
        print(x[0], end=' ')
print(f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for x in b:
    if x[1] == menor:
        print(x[0], end=' ')
