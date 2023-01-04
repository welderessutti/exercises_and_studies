from datetime import date

ano = int(input('Digite o ano. Caso queira o ano atual digite "0": '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\nO ano {ano} é bissexto.')
else:
    print(f'\nO ano {ano} não é bissexto.')

# COLOQUEI ESSAS CONTAS AQUI PRA FACILITAR A VISUALIZAÇÃO DOS RESULTADOS:
print('\na', ano % 4)
print('b', ano % 100)
print('c', ano % 400)
