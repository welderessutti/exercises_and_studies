continua = str('sim')
resposta = str('sim')

while not resposta != continua:
    fat = 1

    n = int(input('Qual o fatorial?: '))

    for fatorial in range(1, n + 1):
        fat = fatorial * fat

    print(fat)
    resposta = str(input('Deseja continuar?: ').lower())

print('Programa encerrado a pedido do usuário.')
