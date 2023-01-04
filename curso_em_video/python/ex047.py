for c in range(1, 51):
    if c % 2 == 0:  # USANDO CONDIÇÃO IF SIMPLES.
        print(c, end=' ')
print('Acabou')

for c in range(2, 51, 2):  # CONFIGURANDO O RANGE. MAIS RÁPIDO.
    print(c, end=' ')
print('Acabou')
