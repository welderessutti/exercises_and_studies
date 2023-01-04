from abc import ABCMeta, abstractmethod
from functools import total_ordering

@total_ordering
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != Conta:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

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


conta_do_guilherme = ContaInvestimento(1700)
conta_do_guilherme.depositar(500)

conta_da_daniela = ContaInvestimento(3)
conta_da_daniela.depositar(1000)

conta_do_paulo = ContaInvestimento(133)
conta_do_paulo.depositar(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print(conta_do_guilherme < conta_da_daniela)

for conta in sorted(contas):
    print(conta)

print(conta_do_guilherme <= conta_da_daniela)
