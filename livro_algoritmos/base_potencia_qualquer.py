base = int(input('Qual a base?: '))
exp = int(input('Qual expoente?: '))
cont = 0

while cont <= exp:
    pot = base ** cont
    cont += 1
    print(pot)
