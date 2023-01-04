dias = int(input('Digite quantos dias você ficou com o carro: '))
km = float(input('Digite quantos Quilometros você rodou no período informado: '))

pagar = dias * 60 + km * 0.15

print(f'Você alugou o carro por {dias:.0f} dia(s) e rodou {km:.1f} Km. O custo total ficou em: R$ {pagar:.2f}')
