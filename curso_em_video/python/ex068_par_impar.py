from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')

cont = 0

while True:

    print('=-' * 15)
    pc = randint(0, 10)
    player = int(input('Digite um valor [0 - 10]: '))
    while player not in range(0, 11):
        print('Opção inválida! Digite novamente.')
        player = int(input('Digite um valor [0 - 10]: '))

    soma = pc + player
    resto = soma % 2

    par_impar = input('Par ou Ímpar? [P/I]: ').strip().upper()
    while par_impar not in 'PI':
        print('Opção inválida! Digite novamente.')
        par_impar = input('Par ou Ímpar? [P/I]: ').strip().upper()

    if par_impar == 'P':
        if resto == 0:
            print(f'-' * 30)
            print(f'Você jogou {player} e computador {pc}. Total de {soma} deu PAR!'
                  f'\nVocê VENCEU!'
                  f'\nVamos jogar novamente...')
            cont += 1
        elif resto == 1:
            print(f'-' * 30)
            print(f'Você jogou {player} e computador {pc}. Total de {soma} deu ÍMPAR!'
                  f'\nVocê PERDEU!')
            break
    elif par_impar == 'I':
        if resto == 1:
            print(f'-' * 30)
            print(f'Você jogou {player} e computador {pc}. Total de {soma} deu ÍMPAR!'
                  f'\nVocê VENCEU!'
                  f'\nVamos jogar novamente...')
            cont += 1
        elif resto == 0:
            print(f'-' * 30)
            print(f'Você jogou {player} e computador {pc}. Total de {soma} deu PAR!'
                  f'\nVocê PERDEU!')
            break

print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')
