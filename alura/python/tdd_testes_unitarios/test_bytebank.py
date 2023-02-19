import pytest
from pytest import mark
from bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000"  # Given
        esperado = 23

        funcionario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_teste.idade()  # When

        assert resultado == esperado  # Then

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entrada = "  Lucas Carvalho   "  # Given
        esperado = "Carvalho"

        lucas = Funcionario(entrada, "11/11/2000", 1111)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado  # Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)
        funcionario_teste.decrescimo_salario()  # When
        resultado = funcionario_teste.salario

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # Given
        esperado = 100

        funcionario_teste = Funcionario("Teste", "11/11/2000", entrada)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000  # Given

            funcionario_teste = Funcionario("Teste", "11/11/2000", entrada)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado  # Then

    def test_retorno_str(self):
        nome, data_nascimento, salario = "Teste", "12/03/2000", 1000  # Given
        esperado = f'Funcionario(Teste, 12/03/2000, 1000)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()  # When

        assert resultado == esperado  # Then
