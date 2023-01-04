print(f'{" LOJAS DEDI DEDI ":=^40}')

preco = float(input('Preço do produto: '))

print('FORMAS DE PAGAMENTO:'
      '\n[ 1 ] à vista dinheiro/cheque'
      '\n[ 2 ] à vista cartão'
      '\n[ 3 ] em até 2x no cartão'
      '\n[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção?: '))

if opcao == 1:
    print(f'Você ganhou 10% de desconto (R$ {(preco * 10) / 100:.2f}).'
          f'\nSua compra de R$ {preco:.2f} vai custar R$ {preco - ((preco * 10) / 100):.2f}.')
elif opcao == 2:
    print(f'Você ganhou 5% de desconto (R$ {(preco * 5) / 100:.2f}).'
          f'\nSua compra de R$ {preco:.2f} vai custar R$ {preco - ((preco * 5) / 100):.2f}.')
elif opcao == 3:
    parcelas = int(input('Em quantas parcelas?: '))
    if parcelas == 1 or parcelas == 2:
        print(f'Sua compra será parcelada em {parcelas}x de R$ {preco / parcelas:.2f} sem juros.'
              f'\nSua compra de R$ {preco:.2f} vai custar R$ {(preco / parcelas) * parcelas:.2f}.')
    else:
        print(f'O número de {parcelas} parcelas é INVÁLIDO para a opção selecionada.')
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas?: '))
    if parcelas >= 3:
        print(f'Sua compra será parcelada em {parcelas}x de R$ {(((preco * 20) / 100) + preco) / parcelas:.2f} com juros.'
              f'\nSua compra de R$ {preco:.2f} vai custar R$ {(((preco * 20) / 100) + preco):.2f}.')
    else:
        print(f'O número de {parcelas} parcelas é INVÁLIDO para a opção selecionada.')
else:
    print(f'A opção {opcao} é INVÁLIDA.')
