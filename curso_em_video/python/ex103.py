def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


nome_jogador = input("Nome do jogador: ")
num_gols = input("Número de Gols: ")

if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0

if nome_jogador.strip() == "":
    ficha(gols=num_gols)
else:
    ficha(nome_jogador, num_gols)
