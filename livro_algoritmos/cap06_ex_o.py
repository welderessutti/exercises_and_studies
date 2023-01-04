a =[]
b = []

for x in range(0, 25):
    a.append(float(input('Digite a temperatura C°: ')))

for z in a:
    fahrenheit = (z * 9/5) + 32
    b.append(fahrenheit)

print(a)
print(b)
