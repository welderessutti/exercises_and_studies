from datetime import date

sexo = str(input('Digite o seu sexo "M" ou "F": ').upper())

if sexo == 'M':

    ano_nasc = int(input('Digite o ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    print(f'\nQuem nasceu em {ano_nasc} e tem {idade} anos em {ano_atual}.')

    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para o alistamento.'
              f'\nSeu alistamento será em {(18 - idade) + ano_atual}.')
    elif idade > 18:
        print(f'Você já deveria ter se alistado há {idade - 18} anos.'
              f'\nSeu alistamento foi em {ano_atual - (idade - 18)}.')
    else:
        print(f'Você tem {idade} anos e deve se alistar IMEDIATAMENTE!')
elif sexo == 'F':
    print('O alistamento é obrigatório somente para pessoas do sexo MASCULINO.')
else:
    print('Sexo inválido.')
