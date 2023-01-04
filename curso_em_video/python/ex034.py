salario = float(input('Digite o seu salário: '))

if salario > 1250.00:
    reajuste = salario + (salario * (10 / 100))
else:
    reajuste = salario + (salario * (15 / 100))

print(f'O seu novo salário vai ser R$ {reajuste:.2f}.')
