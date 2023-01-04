cont = 0
soma = 0

num = int(input('Digite um número: '))

while num >= 0:
    soma = soma + num
    cont += 1
    num = int(input('Digite um número: '))

print(f'\nA soma dos números é: {soma}.')
print(f'A média dos números é: {soma / cont}.')
print(f'O total de valores lidos é: {cont}.')
