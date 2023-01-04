import pytest


def fatorial(n):
    if n < 1:  # Base da recursão
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva


@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
])
def test_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado
