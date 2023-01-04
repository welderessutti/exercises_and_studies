soma = 0
cont = 0

for pares in range(1, 501):
    if pares % 2 == 0:
        soma = soma + pares
        cont += 1

print(soma)
print(cont)
