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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):  # CONTEM UM ERRO GRAVE, O DEPÓSITO É FEITO MESMO NÃO TENDO SALDO PARA TRANSFERIR. EU ARRUMEI NO OUTRO ARQUIVO FINAL QUE EU FIZ.
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


welder = Conta(1988, "Welder", 1000.0, 1000.0)
carmen = Conta(1959, "Carmen", 1000.0, 1000.0)

welder.transfere(3000.0, carmen)

print(welder.saldo)
print(carmen.saldo)

print(Conta.codigo_banco())
print(Conta.codigos_bancos())
