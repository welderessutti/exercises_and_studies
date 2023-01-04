a = []
b = []
c = []

for x in range(0, 20):
    a.append(input('Digite um nome: '))
for x in range(0, 30):
    b.append(input('Digite um nome: '))

c = a[:] + b[:]

print(c)
