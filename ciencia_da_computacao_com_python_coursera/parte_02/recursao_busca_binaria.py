import pytest


def busca_binaria(lista, elemento, minimo=0, maximo=None):
    if maximo is None:
        maximo = len(lista) - 1
    if maximo < minimo:
        return False
    else:
        meio = minimo + (maximo - minimo) // 2
    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, minimo, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, maximo)
    else:
        return meio


abc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.mark.parametrize("lista, valor, esperado", [
    (abc, 10, 9),
    (abc, 1, 0),
    (abc, 5, 4),
    (abc, 8, 7),
    (abc, 2, 1),
    (abc, 88, False),
    (abc, -12, False)
])
def test_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor) == esperado
