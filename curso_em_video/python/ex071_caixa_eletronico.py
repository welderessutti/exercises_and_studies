print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)

num = int(input('Qual valor você quer sacar? R$ '))
nota_50 = nota_20 = nota_10 = nota_1 = 0

if num >= 50:
    while num >= 50:
        num -= 50
        nota_50 += 1
    print(f'Total de {nota_50} cédulas de R$ 50,00.')

if num >= 20:
    while num >= 20:
        num -= 20
        nota_20 += 1
    print(f'Total de {nota_20} cédulas de R$ 20,00.')

if num >= 10:
    while num >= 10:
        num -= 10
        nota_10 += 1
    print(f'Total de {nota_10} cédulas de R$ 10,00.')

if num >= 1:
    while num >= 1:
        num -= 1
        nota_1 += 1
    print(f'Total de {nota_1} cédulas de R$ 1,00.')

print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

# PROFESSOR FEZ ASSIM:

print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)

saque = int(input('Que valor você quer sacar? R$ '))
total = saque
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break

# UMA FORMA MAIS MATEMÁTICA QUE POSTARAM NOS COMENTÁRIOS:

valor = int(input('valor de saque?R$'))
cin = valor // 50
vin = (valor - (cin * 50)) // 20
dez = (valor - ((cin * 50) + (vin * 20))) // 10
um = (valor - ((vin * 20) + (dez * 10) + (cin * 50)))

print('você vai sacar {} em...'.format(valor))

if cin > 0:
    print('{} cédulas de 50 reais '.format(cin))
if vin > 0:
    print('{} cédulas de 20 reais '.format(vin))
if dez > 0:
    print('{} cédulas de 10 reais'.format(dez))
if um > 0:
    print('{} cédulas de 1 reais'.format(um))
