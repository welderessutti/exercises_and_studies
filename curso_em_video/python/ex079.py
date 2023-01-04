lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print(f'Valor {num} adicionado com sucesso!')
    else:
        print(f'Valor {num} duplicado! Não vou adicionar.')

    continuar = str(input('Quer continuar? [S/N]: ').strip().upper())
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Quer continuar? [S/N]: ').strip().upper())

    if continuar == 'N':
        break

lista.sort()

print(f'Você digitou os valores {lista}')
