lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print(f'As medidas dos lados {str(lado1), str(lado2), str(lado3)} formam um triângulo EQUILÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print(f'As medidas dos lados {str(lado1), str(lado2), str(lado3)} formam um triângulo ESCALENO.')
    else:
        print(f'As medidas dos lados {str(lado1), str(lado2), str(lado3)} formam um triângulo ISÓSCELES.')
else:
    print(f'As medidas dos lados {str(lado1), str(lado2), str(lado3)} NÃO formam um triângulo.')
