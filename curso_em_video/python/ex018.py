import math

angulo = float(input('Digite um ângulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
hyp = math.tan(math.radians(angulo))

print(f'O seno é {sen:.2f}, o cosseno é {cos:.2f} e a hipotenusa é {hyp:.2f}.')
