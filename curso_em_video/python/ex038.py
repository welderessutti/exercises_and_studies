n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O PRIMEIRO número é maior.')
elif n2 > n1:
    print(f'O SEGUNDO número é maior.')
else:
    print(f'Os números {n1} e {n2} são IGUAIS.')
