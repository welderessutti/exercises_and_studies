a = []
b = []

for x in range(0, 5):
    a.append(int(input('Digite um número: ')))
    soma = 0
    for z in range(1, a[x] + 1):
        soma += z
    b.append(soma)

print(a)
print(b)
