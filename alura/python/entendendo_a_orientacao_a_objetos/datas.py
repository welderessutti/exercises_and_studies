class Data:
    def __init__(self, d, m, a):
        self.__data = d  # DOIS "UNDERSCORES" ANTES DO NOME DO ATRIBUTO SIGNIFICA QUE ELE É PRIVADO.
        self.__mes = m
        self.__ano = a

    def formatada(self):
        print(f"{self.__data}/{self.__mes}/{self.__ano}")


d = Data(21, 11, 2007)

print(d._Data__data)

d.formatada()

d._Data__data = 5  # APESAR DE SER POSSÍVEL ALTERAR O VALOR DO ATRIBUTO PRIVADO, ISSO É PROIBIDO!

print(d._Data__data)

d.formatada()

d.data = 10  # AQUI É CRIADO UM NOVO ATRIBUTO DESPROTEGIDO DENTRO DA CLASSE DO OBJETO.

print(d.data)

d.formatada()
