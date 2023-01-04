from random import randint
from time import sleep

print('-=-' * 15)
print('TENTE ADIVINHAR O NÚMERO QUE EU PENSEI')
print('-=-' * 15)

num = int(input('De "0" a "5", em que número eu pensei? '))

num_pc = randint(0, 5)

print('PROCESSANDO...')
sleep(2)

print(f'\nEu escolhi "{num_pc}" e você "{num}".')

if num == num_pc:
    print('\n***PARABÉNS*** Você venceu!')
else:
    print('\nVocê perdeu! Tente novamente.')
