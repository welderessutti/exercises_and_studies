cont = 1

a = []
b = []

while cont <= 10:
    a.append(int(input('Digite um número: ')))
    cont += 1

for c in range(0, len(a)):
    if c % 2 == 0:
        b.append(a[c] * 5)
    else:
        b.append(a[c] + 5)

print(f'Matriz A {a}.')
print(f'Matriz B {b}.')
