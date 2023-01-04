from math import sqrt

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

delta = (b ** 2) - (4 * (a * c))
x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)

if delta < 0:
    print(f'Não há solução real para delta {delta}.')
if delta > 0:
    print(f'Há duas soluções reais e diferente para delta {delta}.')
if delta == 0:
    print(f'Há apenas uma solução real para delta {delta}.')

print(f"x' = {x1}")
print(f"x'' = {x2}")

# NÃO SOUBE FAZER COMPLETAMENTE DEVIDO À DA FÓRMULA E DO ENUNCIADO.
# ATUALIZANDO 18/10/2022, CONSEGUI FAZER CORRETAMENTE:

a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))

delta = (b ** 2) - (4 * (a * c))

if delta < 0:
    print(f"A equação não possui resultados reais para delta {delta}.")
elif delta == 0:
    x1 = (- b + sqrt(delta)) / (2 * a)
    print(f"A equação possui apenas um resultado real ou possui dois resultados iguais para delta = {delta}.")
    print(f"x' = {x1}.")
else:
    x1 = (- b + sqrt(delta)) / (2 * a)
    x2 = (- b - sqrt(delta)) / (2 * a)
    print(f"A equação possui dois resultados reais diferentes para delta = {delta}.")
    print(f"x' = {x1}\nx'' = {x2}.")
