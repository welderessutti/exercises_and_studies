num = int(input('Digite um número: '))

cont = soma = 0

maior = num
menor = num
cont += 1
soma += num

resp = input('Deseja continuar? [S/N]: ').strip().upper()

while resp == 'S':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1
    soma += num
    resp = input('Deseja continuar? [S/N]: ').strip().upper()

print(f'Você digitou {cont} números e a média foi {soma / cont}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')

# OUTRO JEITO DE REGISTRAR O MAIOR E MENOR NÚMERO, ACRESCENTAR "OR MAIOR/MENOR == 0", APRENDI DEPOIS DE AVANÇAR NO CURSO:

cont_1 = soma_1 = maior_1 = menor_1 = 0

while True:
    num_1 = int(input('Digite um número: '))
    if num_1 > maior_1 or maior_1 == 0:
        maior_1 = num_1
    if num_1 < menor_1 or menor_1 == 0:
        menor_1 = num_1
    cont_1 += 1
    soma_1 += num_1
    resp_1 = input('Deseja continuar? [S/N]: ').strip().upper()
    while resp_1 not in 'SN':
        print('Opção inválida! Tente novamente.')
        resp_1 = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp_1 == 'N':
        break

print(f'Você digitou {cont_1} números e a média foi {soma_1 / cont_1}.')
print(f'O maior valor foi {maior_1} e o menor foi {menor_1}.')
