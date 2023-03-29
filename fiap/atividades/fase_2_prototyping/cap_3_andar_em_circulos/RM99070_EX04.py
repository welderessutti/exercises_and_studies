fatorial = 1
contador = int(input("Digite os minutos atuais da máquina: "))

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"\nLIBERDADE{fatorial}")
