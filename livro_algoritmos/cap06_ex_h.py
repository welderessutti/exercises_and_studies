a = []
b = [0]

for x in range(0, 20):
    a.append(float(input('Digite um número: ')))

b = a[:]
b.reverse()

print(b)
