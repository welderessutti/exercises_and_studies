laco = 50
soma = 0
cont = 0

while laco <= 70:
    if laco % 2 == 0:
        soma += laco
        cont += 1
    laco += 1
print(f'soma: {soma}')
print(f'média: {soma / cont}')
