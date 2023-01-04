cont = 1
anterior = 0
atual = 1

print(0)
print(1)

while cont <= 100:
    proximo = anterior + atual
    print(proximo)
    anterior = atual
    atual = proximo
    cont += 1
