class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


welder = Conta(1988, "Welder", 1000.0, 1000.0)
carmen = Conta(1959, "Carmen", 1000.0, 1000.0)

welder.transfere(1000.0, carmen)

welder.extrato()
carmen.extrato()
