num = float(input('Digite seu número: '))

if not num < 0:
    if num != 5:
        r = num ** (1/2)
    else:
        r = num ** (1/3)
    print(r)
