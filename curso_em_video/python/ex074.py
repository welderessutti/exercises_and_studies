from random import randint, sample

x = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')

for c in x:
    print(c, end=' ')

print(f'\nO maior valor sorteado: {max(x)}.')
print(f'O menor valor sorteado: {min(x)}.')

# OUTRA MANEIRA MAIS AVANÇADA USANDO MÓDULO "SAMPLE", (PODE USAR PARA FAZER SURPRESINHA MEGA-SENA):

a = tuple(sample(range(0, 11), 5))

print(f'\nOs números sorteados foram {a}.')

print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
