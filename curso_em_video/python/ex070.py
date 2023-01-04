soma = produto_mil = preco_barato = 0
produto_barato = ''

while True:
    produto = input('Nome do Produto: ').strip().title()
    preco = float(input('Preço: R$ '))

    soma += preco

    if preco > 1000:
        produto_mil += 1
    if preco < preco_barato or preco_barato == 0:
        preco_barato = preco
        produto_barato = produto

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        print('Opção inválida! Tente novamente.')
        continuar = input('Quer continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print(f'O total da compra foi R$ {soma:.2f}.'
      f'\nTemos {produto_mil} produtos custando mais de R$ 1.000.00.'
      f'\nO produto mais barato foi {produto_barato} que custa R$ {preco_barato:.2f}.')
