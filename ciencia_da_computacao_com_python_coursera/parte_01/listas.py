lista1 = ["carro", "barco"]
lista2 = lista1
lista3 = [lista1] * 3
lista4 = lista1 * 3

print(lista1)
print(lista2)
print(lista3)
print(lista4)

lista5 = ["carro", "barco"]
lista6 = [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]]
lista7 = ["carro", "barco", "carro", "barco", "carro", "barco"]
lista5[1] = "metrô"

print(lista5)
print(lista6)
print(lista7)

lista8 = ["carro", "barco"]
lista9 = [lista8] * 3
lista10 = lista8 * 3
lista8[1] = "metrô"

print(lista8)
print(lista9)
print(lista10)
