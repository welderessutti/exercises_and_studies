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


lala = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lala)

lala = ordem_inversa(lala)

print(lala)
