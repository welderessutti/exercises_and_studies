soma = 0
cont = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print(f'Você informou {cont} números pares e a soma deles é: {soma}.')
