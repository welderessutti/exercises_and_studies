from random import randint

pc = randint(0, 10)
tentativa = 1

print('Sou seu computador...'
      '\nAcabei de pensar em um número entre 0 e 10.'
      '\nSerá que você consegue adivinhar qual foi?\n')

palpite = int(input('Qual é seu palpite?: '))

while palpite != pc:
    if palpite - pc < 0:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    palpite = int(input('Qual é seu palpite?: '))
    tentativa += 1

print(f'Acertou com {tentativa} tentativa(s). Parabéns!')
print(f'A escolha do computador foi {pc}.\n')

# PROFESSOR FEZ "WHILE" UTILIZANDO VARIÁVEL "TRUE OR FALSE":

acertou = False
tentativa_1 = 0

while not acertou:
    palpite_1 = int(input('Qual é seu palpite?: '))
    tentativa_1 += 1
    if palpite_1 == pc:
        acertou = True
        print(f'Acertou com {tentativa_1} tentativa(s). Parabéns!')
        print(f'A escolha do computador foi {pc}.')
    else:
        if palpite_1 < pc:
            print('Mais... Tente mais uma vez.')
        elif palpite_1 > pc:
            print('Menos... Tente mais uma vez.')
