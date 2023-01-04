n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))

md = (n1 + n2 + n3 + n4) / 4

if md < 7:
    ne = float(input('Nota exame: '))
    md2 = (ne + md) / 2
    if md2 >= 5:
        print(f'APROVADO EM EXAME, sua média foi {md2}.')
    else:
        print(f'REPROVADO! Sua média foi {md2}')
else:
    print(f'APROVADO! Sua média foi {md}.')
