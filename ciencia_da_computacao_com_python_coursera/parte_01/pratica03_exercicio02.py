num = int(input("Digite um número inteiro: "))

igual = False

while not igual and num != 0:
    resto_1 = num % 10
    num = num // 10
    resto_2 = num % 10
    if resto_1 == resto_2:
        igual = True

if igual:
    print("sim")
else:
    print("não")
