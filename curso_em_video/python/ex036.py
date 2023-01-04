casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu salário?: '))
anos = int(input('Em quantos anos vai pagar?: '))

prestacao = float(casa / (anos * 12))
porcentagem = float((prestacao / salario) * 100)

print(f'\nPara pagar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}.')

if porcentagem > 30:
    print(f'\nEmpréstimo NEGADO! A prestação está sendo {porcentagem:.2f} % referente ao salário.')
else:
    print(f'\nEmpréstimo CONCEDIDO! A prestação está sendo {porcentagem:.2f} % referente ao salário.')

# PROFESSOR FEZ USANDO O SALÁRIO MÍMINO POSSÍVEL E NÃO A PORCETAGEM:

minimo = (salario * 30) / 100

if prestacao <= minimo:
    print(f'\nEmpréstimo CONCEDIDO! A prestação está sendo {porcentagem:.2f} % referente ao salário. A parcela máxima permitida é de R$ {minimo}.')
else:
    print(f'\nEmpréstimo NEGADO! A prestação está sendo {porcentagem:.2f} % referente ao salário. A parcela máxima permitida é de R$ {minimo}.')
