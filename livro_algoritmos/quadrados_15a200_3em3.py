cont = 15

while cont <= 200:
    quadrado = cont ** 2
    print(quadrado, end=' ')
    cont += 3

print('\b')
# COM LAÇO "FOR":

for cont_1 in range(15, 201, 3):
    quadrado_1 = cont_1 ** 2
    print(quadrado_1, end=' ')
