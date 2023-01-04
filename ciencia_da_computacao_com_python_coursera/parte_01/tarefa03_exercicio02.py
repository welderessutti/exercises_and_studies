n = int(input("Digite o valor de n: "))

cont = 0
impar = 0

while cont < n:
    if impar % 2 != 0:
        print(impar)
        impar += 1
        cont += 1
    else:
        impar += 1
