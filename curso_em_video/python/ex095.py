time = list()
gols_jogador = list()
jogador = dict()

while True:
    jogador["nome"] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: ').strip())
    for p in range(0, partidas):
        gols_jogador.append(int(input(f'Quantos gols na partida {p + 1}?: ').strip()))

    jogador["gols"] = gols_jogador[:]
    jogador["total"] = sum(gols_jogador)

    time.append(jogador.copy())
    gols_jogador.clear()

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida! Quer continuar? [S/N]: ').strip().upper()
    if continuar == "N":
        break

print('-=' * 30)
print(f'{"cod":<4}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 45)

for i, v in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    dados_jogador = int(input('\nMostrar dados de qual jogador? (999 para parar): '))
    while dados_jogador < 0 or dados_jogador > len(time) - 1 and dados_jogador != 999:
        dados_jogador = int(input('Opção inválida! Mostrar dados de qual jogador? (999 para parar): '))
    if dados_jogador == 999:
        break

    print(f'-- LEVANTAMENTO DO JOGADOR {time[dados_jogador]["nome"]}')

    for a, b in enumerate(time[dados_jogador]["gols"]):
        print(f'\tNo jogo {a + 1} fez {b} gols.')

    print('-' * 45)
