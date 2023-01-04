num = int(input("Digite um número: "))

igual = False

while not igual and num != 0:
    resto_1 = num % 10
    num //= 10
    resto_2 = num % 10
    if resto_1 == resto_2:
        igual = True

if igual:
    print("Há números adjacentes.")
else:
    print("Não há números adjacentes.")
