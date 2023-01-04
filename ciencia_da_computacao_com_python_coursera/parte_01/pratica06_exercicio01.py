def n_primos(n):
    dividendo = 1
    quantidade = 0

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
            quantidade += 1
        dividendo += 1
    return quantidade


num = int(input("Digite um número: "))

print(n_primos(num))
