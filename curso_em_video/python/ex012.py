preco = float(input('Digite o preço do produto: '))

porcentagem_desconto = 5
desconto = preco * (porcentagem_desconto/100)
preco_desconto = preco - desconto

print(f'O preço do produto é {preco:.2f}, aplicando o desconto de {porcentagem_desconto} % você ganha um desconto de R$ {desconto:.2f}, pagando apenas R$ {preco_desconto:.2f}.')
