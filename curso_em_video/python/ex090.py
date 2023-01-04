aluno = dict()

aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')

print(aluno)
