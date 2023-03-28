anterior = 0
atual = 1
num = int(input("Numero: "))

while True:
    print(atual)
    if atual == num:
        print("Ação bem-sucedida!")
        break
    elif atual > num:
        print("A ação falhou...")
        break
    else:
        proximo = anterior + atual
        anterior = atual
        atual = proximo
