def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
                print(" x ", end=" ")
            else:
                print(" = ", end=" ")
        fat *= c
    return fat


print(fatorial(5, show=True))
help(fatorial)
