# List Comprehension:
def proximo_ano(idade):
    return idade + 1


idades = [21, 40, 19, 28, 20]

idades = [proximo_ano(idade) for idade in idades if idade > 21]

print(idades)


class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Código {self.codigo} Saldo {self.saldo}<<]"


class Conta(ContaCorrente):

    def __init__(self, codigo, agencia):
        super().__init__(codigo)
        self.agencia = agencia


welder = Conta(123, 555)

print(welder.saldo, welder.codigo, welder.agencia)
