num = int(input('Digite um número para calcular seu Fatorial: '))
cont = 1
fat = 1

print(f'Calculando {num}! = ', end='')

while cont <= num:
    print(f'{cont}', end='')
    print(f' x ' if cont < num else ' = ', end='')
    fat *= cont
    cont += 1

print(f'{fat}')

# PROFESSOR FEZ ASSIM:

num1 = int(input('Digite um número para calcular seu Fatorail: '))
cont1 = num1
fat1 = 1

print(f'Calculando {num1}! = ', end='')

while cont1 > 0:
    print(f'{cont1}', end='')
    print(f' x ' if cont1 > 1 else ' = ', end='')
    fat1 *= cont1
    cont1 -= 1

print(f'{fat1}')
