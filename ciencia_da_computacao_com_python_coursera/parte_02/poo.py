class Cachorro:
    def __init__(self, raca, idade, nome, cor):
        self.raca = raca
        self.idade = idade
        self.nome = nome
        self.cor = cor

    def latir(self):
        return print("au-au")


rex = Cachorro('vira-lata', 2, 'Bobby', 'marrom')

rex.raca = "labrador"
rex.latir()
print(rex.raca)
print(rex)

print()


class Lista:
    def append(self, elemento):
        return "Oops! Este objeto não é uma lista"


lista = []

a = Lista()
b = a.append(7)

lista.append(b)

print(lista)
print(b)
