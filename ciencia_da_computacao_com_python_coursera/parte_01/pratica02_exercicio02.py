import math

a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))

delta = (b ** 2) - (4 * (a * c))

if delta < 0:
    print(f"esta equação não possui raízes reais")
elif delta == 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    print(f"a raiz desta equação é {x1}")
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    if x1 != x2:
        if x1 < x2:
            print(f"as raízes da equação são {x1} e {x2}")
        else:
            print(f"as raízes da equação são {x2} e {x1}")
    else:
        print(f"as raízes da equação são {x1} e {x2}")
