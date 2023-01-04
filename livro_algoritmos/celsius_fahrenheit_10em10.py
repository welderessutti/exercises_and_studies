# fah = (cel * (9/5)) + 32

# COM LAÇO "FOR":

for celsius in range(10, 101, 10):
    fahrenheit = (celsius * (9/5)) + 32
    print(f'{celsius:.1f} C°', end=' ')
    print(f'{fahrenheit} F°')

# COM LAÇO "WHILE":

cont = 10

while cont <= 100:
    fahrenheit_2 = (cont * (9/5)) + 32
    print(f'{cont} C°', end=' ')
    print(f'{fahrenheit_2} F°')
    cont += 10
