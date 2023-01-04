peso = float(input(f'Peso da 1ª pessoa: '))
menor = peso
maior = peso

for pesos in range(2, 6):
    peso = float(input(f'Peso da {pesos}ª pessoa: '))
    if peso > menor and peso > maior:
        maior = peso
    elif peso < maior and peso < menor:
        menor = peso

print(f'O maior peso lido foi de {maior} Kg.')
print(f'O menor peso lido foi de {menor} Kg.')

# PROFESSOR FEZ DESTA FORMA:

maior_1 = 0
menor_1 = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior_1 = peso
        menor_1 = peso
    else:
        if peso > maior_1:
            maior_1 = peso
        if peso < menor_1:
            menor_1 = peso

print(f'O maior peso lido foi de {maior_1} Kg.')
print(f'O menor peso lido foi de {menor_1} Kg.')
