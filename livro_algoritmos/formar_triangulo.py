l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l2 == l3:
        print(f'Os lados {l1}, {l2} e {l3} formam um triângulo equilátero.')
    elif l1 == l2 and l2 != l3 or l1 == l3 and l2 != l1 or l2 == l3 and l1 != l3:
        print(f'Os lados {l1}, {l2} e {l3} formam um triângulo isósceles.')
    elif l1 != l2 and l2 != l3:
        print(f'Os lados {l1}, {l2} e {l3} formam um triângulo escaleno.')
else:
    print('Os lados não formam um triângulo.')
