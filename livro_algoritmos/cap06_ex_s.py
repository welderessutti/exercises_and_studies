a = []
b = []
c = []
cont = 0

while cont < 12:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        a.append(num)
        cont += 1
    else:
        b.append(num)
        cont += 1

c = a[:] + b[:]

print(a)
print(b)
print(c)
