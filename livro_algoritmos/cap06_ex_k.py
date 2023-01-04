a = []
b = []

for x in range(0, 10):
    a.append(int(input('Digite um número: ')))
    b.append(a[x] * -1)

# OU

for z in a:
    b.append(z * -1)

print(a)
print(b)
