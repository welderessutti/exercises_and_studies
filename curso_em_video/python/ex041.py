from datetime import date

ano_nasc = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

if ano_nasc <= ano_atual:
    print(f'\nO atleta tem {idade} anos.')
    if idade <= 9:
        print('Classificação: MIRIM.')
    elif idade <= 14:
        print('Classificação: INFANTIL.')
    elif idade <= 19:
        print('Classificação: JUNIOR.')
    elif idade <= 25:
        print('Classificação: SÊNIOR.')
    else:
        print('Classificação: MASTER.')
else:
    print('\nAno inválido, digite novamente.')
