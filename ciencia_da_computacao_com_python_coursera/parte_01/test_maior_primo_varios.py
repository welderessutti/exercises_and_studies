def maior_primo(n):
    dividendo = 1
    ultimo_primo = 0

    while dividendo <= n:
        divisor = 1
        cont = 0
        while divisor <= dividendo:
            if dividendo % divisor == 0:
                cont += 1
                divisor += 1
            else:
                divisor += 1
        if cont == 2:
            ultimo_primo = dividendo
        dividendo += 1
    return ultimo_primo


def test_maior_primo100():
    assert maior_primo(100) == 97
