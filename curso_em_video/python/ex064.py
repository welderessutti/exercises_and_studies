parar = False

soma = cont = 0

while not parar:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        parar = True

print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

# PROFESSOR FEZ ASSIM:

num_1 = cont_1 = soma_1 = 0

num_1 = int(input('Digite um número [999 para parar]: '))

while num_1 != 999:
    soma_1 += num_1
    cont_1 += 1
    num_1 = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {cont_1} números e a soma entre eles foi {soma_1}.')
