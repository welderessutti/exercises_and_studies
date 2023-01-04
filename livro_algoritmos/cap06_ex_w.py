a = []
b = []
c = []

for x in range(0, 10):
    a.append(int(input('Digite um valor: ')))
    b.append(int(input('Digite outro valor: ')))
    c.append((a[x] + b[x]) ** 2)

print(a)
print(b)
print(c)
