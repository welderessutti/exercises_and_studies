a = []
b = []
c = []
cont = 0

while cont < 20:
    num = int(input('Digite um valor: '))
    if num % 2 == 0 and num % 3 == 0:
        a.append(num)
        cont += 1
    if num % 5 == 0:
        b.append(num)
        cont += 1

c = a[:] + b[:]

print(a)
print(b)
print(c)
