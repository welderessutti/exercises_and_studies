a = []
par = impar = 0

for x in range(0, 30):
    a.append(int(input('Digite um valor: ')))

for z in a:
    if z % 2 == 0:
        par += 1
    else:
        impar += 1

print(a)
print(f'números pares {par}.')
print(f'números ímpares {impar}.')
