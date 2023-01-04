a = []
b = []
c = []

for x in range(0, 20):
    a.append(float(input('Digite um número: ')))
    b.append(float(input('Digite outro número: ')))
    c.append(a[x] - b[x])

print(a)
print(b)
print(c)
