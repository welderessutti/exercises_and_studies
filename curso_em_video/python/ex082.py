todos = []
pares = []
impares = []
pos = 0

while True:
    todos.append(int(input('Digite um número: ')))

    if todos[pos] % 2 == 0:
        pares.append(todos[pos])
    else:
        impares.append(todos[pos])

    pos += 1

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print(f'A lista completa é {todos}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')

# USANDO O "FOR":

lista = []
pares_1 = []
impares_1 = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar? [S/N]: ').strip().upper()

    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

for c in lista:
    if c % 2 == 0:
        pares_1.append(c)
    else:
        impares_1.append(c)

print(f'A lista completa é {lista}.')
print(f'A lista de pares é {pares_1}.')
print(f'A lista de ímpares é {impares_1}.')
