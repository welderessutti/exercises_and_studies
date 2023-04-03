# Inicia a variável fatorial com o valor 1 e recebe como input os minutos do usuário:
fatorial = 1
contador = int(input("Digite os minutos atuais da máquina: "))

# Executa um laço do tipo while, fazendo a multiplicação do fatorial e decrescendo 1 da variável contador,
# até que o valor da variável contador seja maior que zero:
while contador > 0:
    fatorial *= contador
    contador -= 1

# Lança o output informando a senha:
print(f"\nLIBERDADE{fatorial}")
