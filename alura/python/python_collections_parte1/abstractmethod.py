from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != Conta:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        return self._saldo < other._saldo

    def __str__(self):
        return f">>Codigo {self._codigo} Saldo {self._saldo}<<"

    @abstractmethod
    def passa_o_mes(self):
        pass

    def depositar(self, valor):
        self._saldo += valor


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):

    def __eq__(self, other):
        if type(other) != ContaInvestimento:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def passa_o_mes(self):
        self._saldo = 100


welder = ContaInvestimento(555)
welder.passa_o_mes()

print(welder._codigo, welder._saldo)
