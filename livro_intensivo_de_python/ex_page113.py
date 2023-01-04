for num in range(1, 21):
    print(num, end=' ')

milions = list(range(1, 1000001))
for milion in milions:
    print(milion)

print(min(milions))
print(max(milions))
print(sum(milions))

cubos = []
for cubo in range(1, 11):
    cubo = cubo ** 3
    cubos.append(cubo)
print(cubos)

cubase = cubos[:]
print(cubase)

cubase.append(555)
print(cubase)

print('primeiros 3 numeros:')
for cuba in cubase[:3]:
    print(cuba)
