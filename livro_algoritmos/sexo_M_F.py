nome = str(input('Digite o seu nome completo: '))
sexo = str(input('Digite o seu sexo "M" ou "F": ').upper())

if sexo == 'M' or sexo == 'F':
    if sexo == 'M':
        print(f'Ilmo. Sr. {nome}.')
    else:
        print(f'Ilma. Sra. {nome}.')
else:
    print('Sexo informado inválido.')
