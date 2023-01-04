import classe_comparacao_de_desempenho
import pytest


class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return classe_comparacao_de_desempenho.Ordenador()

    @pytest.fixture
    def lista_quase(self):
        c = classe_comparacao_de_desempenho.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def lista_aleatoria(self):
        c = classe_comparacao_de_desempenho.ContaTempos()
        return c.lista_aletoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True

    def test_bolha_curta_aleat(self, o, lista_aleatoria):
        o.short_bubble_sort(lista_aleatoria)
        assert self.esta_ordenada(lista_aleatoria)

    def test_selecao_direta_aleat(self, o, lista_aleatoria):
        o.selecao_direta(lista_aleatoria)
        assert self.esta_ordenada(lista_aleatoria)

    def test_bolha_curta_quase(self, o, lista_quase):
        o.short_bubble_sort(lista_quase)
        assert self.esta_ordenada(lista_quase)

    def test_selecao_direta_quase(self, o, lista_quase):
        o.selecao_direta(lista_quase)
        assert self.esta_ordenada(lista_quase)
