from bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000"  # Given
        esperado = 23

        funcionario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_teste.idade()  # When

        assert resultado == esperado
