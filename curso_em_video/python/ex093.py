dados = dict()

dados['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
dados['gols'] = list()  # AQUI GEREI A LISTA DIRETAMENTE DENTRO DO DICIONÁRIO.

for c in range(0, partidas):
    dados['gols'].insert(c, int(input(f'Quantos gols na partida {c}?: ')))  # DEPOIS INCLUÍ CADA VALOR NA LISTA.

dados['total'] = sum(dados["gols"])

print('-=' * 30)
print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')

print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for c, b in enumerate(dados["gols"]):
    print(f'\t=> Na partida {c}, fez {b} gols.')

print(f'Foi um total de {dados["total"]} gols.\n')

# OUTRA FORMA DECLARANDO A LISTA ANTES E DEPOIS INCLUINDO DENTRO DA LISTA.
print('-=' * 30)

dados = dict()
gols = list()

dados['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}?: ')))

dados['gols'] = gols[:]
dados['total'] = sum(gols)

print('-=' * 30)
print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')

print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for c, b in enumerate(dados["gols"]):
    print(f'\t=> Na partida {c}, fez {b} gols.')

print(f'Foi um total de {dados["total"]} gols.')
