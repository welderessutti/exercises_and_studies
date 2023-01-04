a = []
b = []
c = []
d = []

for x in range(0, 6):
    a.append(int(input('Digite um número: ')))
    b.append(int(input('Digite outro número: ')))

for y in range(0, len(a)):
    if y % 2 == 1:
        c.append(a[y])
    else:
        d.append(a[y])

for z in range(0, len(b)):
    if z % 2 == 1:
        c.append(b[z])
    else:
        d.append(b[z])

print(a)
print(b)
print(c)
print(d)
