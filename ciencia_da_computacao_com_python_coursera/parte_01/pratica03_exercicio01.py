num = int(input("Digite um número inteiro: "))

cont = 0
divisor = 1

while divisor <= num:
    if num % divisor == 0:
        cont += 1
        divisor += 1
    else:
        divisor += 1

if cont == 2:
    print("primo")
else:
    print("não primo")
