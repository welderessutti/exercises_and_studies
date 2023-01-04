num = int(input("Digite um número: "))
soma = 0

while num != 0:
    soma += num % 10
    num //= 10

print(soma)
