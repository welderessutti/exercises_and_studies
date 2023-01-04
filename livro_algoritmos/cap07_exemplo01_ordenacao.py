a = []
b = []
x = 0

for c in range(0, 10):
    a.append(int(input(f'Digite o {c + 1}º número: ')))
    b.append(a[c] / 5)

for y in range(0, 9, 1):
    for z in range(y + 1, 10, 1):
        if b[y] < b[z]:
            x = b[y]
            b[y] = b[z]
            b[z] = x

print(b)
