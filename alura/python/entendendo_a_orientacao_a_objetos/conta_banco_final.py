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

    def __pode_sacar(self, valor):
        saldo_total = self.__saldo + self.__limite
        return valor <= saldo_total

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            return True
        else:
            print(f"Não há saldo suficiente para o saque de R$ {valor}.")
            return False

    def transfere(self, valor, destino):
        if self.saca(valor):
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
        return {"BB": '001', "Caixa": "104", "Bradesco": "237"}


welder = Conta(1988, "Welder", 1000.0, 1000.0)
carmen = Conta(1959, "Carmen", 1000.0, 1000.0)

welder.transfere(3000.0, carmen)

print(welder.saldo)
print(carmen.saldo)

print(Conta.codigo_banco())
print(Conta.codigos_bancos())

welder.limite = 5000.0

print(welder.limite)
