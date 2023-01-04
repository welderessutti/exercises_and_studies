from random import randint
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']

print('Suas opções:'
      '\n[ 0 ] PEDRA'
      '\n[ 1 ] PAPEL'
      '\n[ 2 ] TESOURA')
user = int(input('Qual é a sua jogada?: '))
computer = randint(0, 2)

if user == 0 or user == 1 or user == 2:
    print('\n*JO*')
    sleep(1)
    print('*KEM*')
    sleep(1)
    print('*PÔ!*\n')
    sleep(1)
    print('-=' * 15)
    print(f'O computador escolheu {lista[computer]}.')
    print(f'E o jogador escolheu {lista[user]}.')
    print('-=' * 15)

    if lista[computer] == lista[user]:
        print('\n\033[1;33;40mEMPATE, TENTE NOVAMENTE.\033[m')
    elif computer == 0:
        if user == 1:
            print('\n\033[1;34;40mJOGADOR VENCEU!\033[m')
        elif user == 2:
            print('\n\033[1;31;40mCOMPUTADOR VENCEU!\033[m')
    elif computer == 1:
        if user == 0:
            print('\n\033[1;31;40mCOMPUTADOR VENCEU!\033[m')
        elif user == 2:
            print('\n\033[1;34;40mJOGADOR VENCEU!\033[m')
    elif computer == 2:
        if user == 0:
            print('\n\033[1;34;40mJOGADOR VENCEU!\033[m')
        elif user == 1:
            print('\n\033[1;31;40mCOMPUTADOR VENCEU!\033[m')
else:
    print('\n\033[1;31;40m[ERROR] Opção inválida. Tente novamante.\033[m')
