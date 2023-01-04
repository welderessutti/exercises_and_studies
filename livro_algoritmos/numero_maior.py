p1 = float(input('Digite o primeiro peso: '))
p2 = float(input('Digite o segundo peso: '))
p3 = float(input('Digite o terceiro peso: '))

x = p1

if x < p2:
    x = p2
if x < p3:
    x = p3

print(x)
