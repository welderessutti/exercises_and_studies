import math

a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))

delta = (b ** 2) - (4 * (a * c))

if delta < 0:
    print(f"A equação não possui resultados reais para delta {delta}.")
elif delta == 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    print(f"A equação possui apenas um resultado real ou possui dois resultados iguais para delta = {delta}.")
    print(f"x' = {x1}.")
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print(f"A equação possui dois resultados reais para delta = {delta}.")
    print(f"x' = {x1}\nx'' = {x2}.")
