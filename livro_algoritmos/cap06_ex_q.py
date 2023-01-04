a = []
b = []

for x in range(0, 15):
    a.append(float(input('Digite um valor: ')))
    if x % 2 == 0:
        b.append(a[x] / 2)
    else:
        b.append(a[x] * 1.5)

print(a)
print(b)
