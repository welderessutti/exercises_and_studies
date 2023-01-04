a = []
impar = 0

for x in range(0, 10):
    a.append(int(input('Digite um valor: ')))
    if a[x] % 2 == 1:
        impar += 1

print(f'O total de números ímpares é {impar} e a porcentagem é {(impar * 100) / len(a)} %.')
