a = []

num = int(input('Digite a tabuada: '))

for x in range(1, 11):
    print(f'{num} x {x} = {num * x}')
    a.append(num * x)

print(a)
