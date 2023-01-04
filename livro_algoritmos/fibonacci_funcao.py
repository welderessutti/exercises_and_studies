def fibonacci(n):
    anterior = 0
    atual = 1
    proximo = 0
    for a in range(1, n):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
    return proximo


print(fibonacci(100))  # DIGITAR O TERMO DESEJADO.
