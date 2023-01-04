from math import ceil, trunc

numero = float(input('Digite um número Real: '))

print(f'A porção inteira do número é {int(numero)}') # inteiro
print(f'A porção inteira do número é {ceil(numero)}') # arredondamento
print(f'A porção inteira do número é {trunc(numero)}') # truncar
