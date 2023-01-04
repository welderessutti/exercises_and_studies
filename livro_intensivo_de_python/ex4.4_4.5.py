lista = list(range(1, 1000001))

for num in lista:
    print(num)

print(min(lista))
print(max(lista))
print(sum(lista))

lista_1 = list(range(1, 11))

cubos = [num_1 ** 3 for num_1 in lista_1]

print(cubos[-3:])
