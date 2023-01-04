cont = 1
soma = 0

a = []

while cont <= 5:
    a.append(int(input('Digite um número: ')))
    cont += 1

for c in a:
    if c % 2 == 1:
        soma += c

print(a)
print(soma)
