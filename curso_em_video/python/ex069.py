pessoa_maior = homem_total = mulher_menos_20 = 0

while True:
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()

    if idade >= 18:
        pessoa_maior += 1
    if sexo == 'M':
        homem_total += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1

    continuar = input('Quer continuar [S/N]?: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]?: ').strip().upper()
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {pessoa_maior}.'
      f'\nAo todo temos {homem_total} homens cadastrados.'
      f'\nE temos {mulher_menos_20} mulheres com menos de 20 anos.')
