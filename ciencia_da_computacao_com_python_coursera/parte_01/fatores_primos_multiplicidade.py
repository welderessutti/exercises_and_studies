n = int(input("Digite um número inteiro > 1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n /= fator
    if multiplicidade > 0:
        print(f"Fator {fator} multipilicidade = {multiplicidade}")
    fator += 1
    multiplicidade = 0
