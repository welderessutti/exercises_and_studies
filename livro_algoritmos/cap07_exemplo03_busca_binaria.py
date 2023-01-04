a = []
b = []
c = []
x = 0

for y in range(0, 5):
    a.append(int(input("Digite um número: ")))

for w in range(0, 5):
    b.append(int(input("Digite um número: ")))

for z in range(0, 10):
    if z <= 4:
        c.append(a[z])
    else:
        c.append(b[z - 5])

for i in range(0, 9):
    for j in range(i + 1, 10):
        if c[i] > c[j]:
            x = c[i]
            c[i] = c[j]
            c[j] = x

resp = input("Deseja pesquisar um número? [S/N]: ").strip().upper()
while resp == "S":

    pesquisa = int(input("Quer pesquisar qual número?: ").strip())

    comeco = 0
    final = 9
    acha = False

    while comeco <= final and acha is False:
        meio = (comeco + final) // 2
        
        if pesquisa == c[meio]:
            acha = True
        else:
            if pesquisa < c[meio]:
                final = meio - 1
            else:
                comeco = meio + 1

    if acha is True:
        print(f"O número {pesquisa} foi localizado na posição {meio}.")
    else:
        print(f"O número {pesquisa} não foi localizado.")
    
    resp = input("Deseja continuar? [S/N]").strip().upper()
    if resp == "N":
        break

print(c)
