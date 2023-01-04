num = int(input('Digite um número: '))
maior = num
menor = num

while num >= 0:
    if num > menor and num > maior:
        maior = num
    elif num < maior and num < menor:
        menor = num
    print(maior, menor)
    num = int(input('Digite um número: '))
print(f'O maior número foi {maior} e o menor foi {menor}.')

# OU COM LISTA USANDO "MAX" E "MIN".

lista = []
num_1 = int(input('Digite um número: '))

while num_1 >= 0:
    lista.append(num_1)
    num_1 = int(input('Digite um número: '))
print(f'O maior número foi {max(lista)} e o menor foi {min(lista)}.')
print(lista)
