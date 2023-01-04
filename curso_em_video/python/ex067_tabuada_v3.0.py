while True:
    cont = 1
    num = int(input('Quer ver a tabuada de qual valor?: '))
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

# COM LAÇO "FOR":

while True:
    num = int(input('Quer ver a tabuada de qual valor?: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
