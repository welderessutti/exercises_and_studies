def maximo(x, y, z):
    if x > y > z or x > z > y:
        return x
    elif y > x > z or y > z > x:
        return y
    else:
        return z


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

print(maximo(a, b, c))
