soma = 0

a = []

while True:
    a.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

for c in a:
    if c % 2 == 0:
        soma += c

print(a)
print(f'A soma dos valores pares é: {soma}.')
