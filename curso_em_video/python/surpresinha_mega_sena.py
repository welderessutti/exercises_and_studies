from random import sample

while True:
    dezenas = int(input('Quantas dezenas você quer [6 a 15]?: '))
    if 6 <= dezenas <= 15:
        break
    else:
        print("Opção inválida. Apenas dezenas de [6 a 15].\n")

while True:
    jogos = int(input('Quantos jogos você quer?: '))
    if jogos > 0:
        break
    else:
        print("Opção inválida. No mínino 1 jogo.\n")

for c in range(0, jogos):
    x = sample(range(1, 26), dezenas)
    print(x)
