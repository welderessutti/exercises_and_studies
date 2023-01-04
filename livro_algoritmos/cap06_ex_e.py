a = []
b = []

for x in range(0, 15):
    a.append(int(input('Digite um número: ')))
    fat = a[x]
    for z in range(a[x] - 1, 0, -1):
        fat *= z
    b.append(fat)

print(a)
print(b)
