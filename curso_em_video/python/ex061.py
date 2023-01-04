# COM LAÇO "WHILE":

print('Gerador de PA')
print('-=' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')

# COM LAÇO "FOR" DO MEU JEITO:

print('Gerador de PA')
print('-=' * 10)

termo_1 = int(input('Primeiro termo: '))
razao_1 = int(input('Razão da PA: '))

for c in range(termo_1, razao_1 * 10 + termo_1, razao_1):
    print(f'{c} -> ', end='')
print('FIM')

# COM LAÇO "FOR" FEITO PRO OUTRA PESSOA:

print('Gerador de PA')
print('-=' * 10)

termo_2 = int(input('Primeiro termo: '))
razao_2 = int(input('Razão da PA: '))

for c in range(1, 11):
    print(f'{termo_2} -> ', end='')
    termo_2 += razao_2
print('FIM')
