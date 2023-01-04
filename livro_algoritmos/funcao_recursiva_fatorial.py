def fatorial(n):
    while not n <= 1:
        return n * fatorial(n - 1)
    return 1


a = int(input("Digite um número: "))

print(fatorial(a))
