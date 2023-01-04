salario = float(input('Digite o salário do colaborador: '))

porcentagem_aumento = 20
aumento = salario * (porcentagem_aumento/100)
salario_aumento = salario + aumento

print(f'O salário do colaborador é {salario:.2f}, aplicando o aumento de {porcentagem_aumento} % vai acrescentar R$ {aumento:.2f} no salário, totalizando R$ {salario_aumento:.2f}.')
