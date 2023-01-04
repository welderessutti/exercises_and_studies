from datetime import datetime

dados = dict()

dados['nome'] = input('Nome: ').strip().title()
nascimento = int(input('Ano de Nascimento: ').strip())
dados['idade'] = datetime.today().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): ').strip())

if dados['ctps'] != 0:
    dados['contratação'] = int(input(f'Ano de Contratação: ').strip())
    dados['salário'] = float(input('Salário: ').strip())
    dados['aposentadoria'] = (dados['contratação'] + 35) - nascimento

for k, v in dados.items():
    print(f'- {k} tem o valor {v}.')
