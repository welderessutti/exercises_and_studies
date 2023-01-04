def ordem_inversa(lista):
    cont = 0
    cont_1 = -1
    for a in range(len(lista) // 2):
        x = lista[cont]
        lista[cont] = lista[cont_1]
        lista[cont_1] = x
        cont += 1
        cont_1 -= 1
    return lista


sequencia = []

while True:
    num = int(input("Digite um número: "))
    if num != 0:
        sequencia.append(num)
    else:
        break

sequencia_invertida = ordem_inversa(sequencia)

for n in sequencia_invertida:
    print(n)
