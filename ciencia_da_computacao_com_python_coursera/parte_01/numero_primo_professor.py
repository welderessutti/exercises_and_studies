# ESSA FUNÇÃO FOI O PROFESSOR QUE DESENVOLVEU, TEM BUG PARA OS NÚMEROS 1 E 2. O 2 EU CORRIGI.

def primo(x):
    fator = 2
    while x % fator != 0 and fator <= x / 2:
        fator += 1
    if x % fator == 0 and x != 2:  # CORRIGI O 2 AQUI.
        return False
    else:
        return True


n = int(input("Digite um número inteiro: "))

while n > 0:
    if primo(n):
        print(f"{n} é primo!")
    else:
        print(f"{n} não é primo =(")
    n = int(input("Digite um número inteiro: "))
