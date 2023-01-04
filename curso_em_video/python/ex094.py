pessoas = list()
dados = dict()
total_idade = 0

while True:
    dados["nome"] = input('Nome: ').strip().title()
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = input('Sexo [M/F]: ').strip().upper()
    dados["sexo"] = sexo
    dados["idade"] = int(input('Idade: ').strip())

    total_idade += dados["idade"]
    pessoas.append(dados.copy())

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = input('Quer continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {total_idade / len(pessoas):.2f}.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}', end=' ')

print(f'\nD) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p["idade"] >= total_idade / len(pessoas):
        for k, v in p.items():
            print(f'\t{k} = {v}', end='; ')
        print('\n')

print('<< ENCERRADO >>')
