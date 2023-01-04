a = []
soma = 0

for x in range(0, 20):
    a.append(float(input('Digite um valor: ')))

for z in a:
    soma += z

media = soma / 20

print(a)
print(max(a))
print(min(a))
print(media)
