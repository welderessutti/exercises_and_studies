a = []
b = []
c = []
d = []

for x in range(0, 5):
    a.append(float(input('Digite um número para "a": ')))
    b.append(float(input('Digite um número para "b": ')))
    c.append(float(input('Digite um número para "c": ')))

d = a[:] + b[:] + c[:]

print(a)
print(b)
print(c)
print(d)
