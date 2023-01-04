def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x


def leitura_1():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x


print(leitura())
