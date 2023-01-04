def delta(a, b, c):
    res = (b ** 2) - (4 * (a * c))
    return res


def raiz_1(a, b, d):
    import math
    res = (- b + math.sqrt(d)) / (2 * a)
    return res


def raiz_2(a, b, d):
    import math
    res = (- b - math.sqrt(d)) / (2 * a)
    return res


def imprime_resultado(a, b, c):
    delta_calculo = delta(a, b, c)

    if delta_calculo < 0:
        print(f"A equação não possui resultados reais para delta {delta_calculo}.")
    elif delta_calculo == 0:
        x1 = raiz_1(a, b, delta_calculo)
        print(f"A equação possui apenas um resultado real ou possui dois resultados iguais para delta = {delta_calculo}.")
        print(f"x' = {x1}.")
    else:
        x1 = raiz_1(a, b, delta_calculo)
        x2 = raiz_2(a, b, delta_calculo)
        print(f"A equação possui dois resultados reais para delta = {delta_calculo}.")
        print(f"x' = {x1}\nx'' = {x2}.")


def main():
    a = float(input("Digite um valor para a: "))
    b = float(input("Digite um valor para b: "))
    c = float(input("Digite um valor para c: "))
    imprime_resultado(a, b, c)


main()
