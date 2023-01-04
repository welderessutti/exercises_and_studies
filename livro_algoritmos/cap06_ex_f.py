a = []
b = []
c = []

for x in range(0, 15):
    a.append(int(input('Digite um número: ')))
    b.append(int(input('Digite outro número: ')))

c.append(a[:] + b[:])

print(a)
print(b)
print(c)
