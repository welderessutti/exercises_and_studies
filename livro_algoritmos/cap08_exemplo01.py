a = []
t = ""

for x in range(0, 3):
    a.append([])
    a[x].append(input("Nome: "))
    a[x].append(input("Endereço: "))
    a[x].append(input("Código Postal: "))
    a[x].append(input("Bairro: "))
    a[x].append(input("Telefone: "))

for y in range(0, 2):
    for z in range(y + 1, 3):
        if a[y][0] > a[z][0]:
            for w in range(0, 5):
                t = a[y][w]
                a[y][w] = a[z][w]
                a[z][w] = t

print(a)
