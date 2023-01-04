a = []
b = []

for x in range(0, 12):
    a.append(int(input('Digite um valor: ')))
    if a[x] % 2 == 1:
        b.append(a[x] * 2)

print(a)
print(b)
