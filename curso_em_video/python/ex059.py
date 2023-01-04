sair = False

primeiro = int(input('Primeiro valor: ').strip())
segundo = int(input('Segundo valor: ').strip())

while not sair:  # PROFESSOR USOU: WHILE OPCAO != 5. NÃO SENDO NECESSÁRIO O "ELIF OPÇÃO == 5", MAS TEM QUE TER A VARIÁVEL OPÇÃO ANTES DO LAÇO.
    print('\t[ 1 ] somar'
          '\n\t[ 2 ] multiplicar'
          '\n\t[ 3 ] maior'
          '\n\t[ 4 ] novos números'
          '\n\t[ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção?: ').strip())

    if opcao == 1:
        print(f'A soma entre {primeiro} + {segundo} é: {primeiro + segundo}.')
    elif opcao == 2:
        print(f'A multiplicação entre {primeiro} x {segundo} é: {primeiro * segundo}.')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'Entre {primeiro} e {segundo} o maior valor é: {primeiro}.')
        elif primeiro < segundo:
            print(f'Entre {primeiro} e {segundo} o maior valor é: {segundo}.')
        elif primeiro == segundo:
            print(f'Os números {primeiro} e {segundo} são iguais.')
    elif opcao == 4:
        print('Informe os novos números:')
        primeiro = int(input('Primeiro valor: ').strip())
        segundo = int(input('Segundo valor: ').strip())
    elif opcao == 5:
        print('Finalizando...')
        sair = True
    else:
        print('Opção inválida. Tente novamente.')
    print(f'=-=' * 10)

print('Fim do programa. Volte sempre!')
