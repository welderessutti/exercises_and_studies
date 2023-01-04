n = int(input("Digite o valor de n: "))

fat = 1
cont = 1

while cont <= n:
    fat *= cont
    cont += 1

print(fat)
