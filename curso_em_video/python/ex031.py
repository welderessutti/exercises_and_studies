distancia = float(input('Digite a distância em Km: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'A distância da sua viagem é de {distancia} Km e o valor da passagem ficou em R$ {preco:.2f}.')
