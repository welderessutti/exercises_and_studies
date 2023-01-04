def maximo(x, y):
    if x > y:
        return x
    else:
        return y


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(maximo(a, b))
