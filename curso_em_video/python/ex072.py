extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {extenso[num]}.')

# PROFESSOR FEZ ASSIM:

extenso_1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
             'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num_1 = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num_1 <= 20:
            break
        print('Tente novamante.', end=' ')
    print(f'Você digitou o número {extenso_1[num_1]}.')

    while True:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
        if continuar in 'SN':
            break
        print('Opção inválida!', end=' ')

    if continuar == 'N':
        break
