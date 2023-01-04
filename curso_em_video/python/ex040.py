nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))

media = (nota_1 + nota_2) / 2

print(f'\nTirando {nota_1:.1f} e {nota_2:.1f} a média do aluno é {media:.1f}')

if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
