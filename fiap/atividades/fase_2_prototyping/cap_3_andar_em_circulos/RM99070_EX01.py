# Recebe como input o tipo de assinatura e faturamento anual do usuário:
assinatura = input("Tipo de assinatura: ").strip().upper()
faturamento_anual = float(input("Faturamento anual: "))

# Verifica o valor da variável assinatura, e atribui o percentual da assinatura à variável porcentagem:
if assinatura == "BASIC":
    porcentagem = 0.3
elif assinatura == "SILVER":
    porcentagem = 0.2
elif assinatura == "GOLD":
    porcentagem = 0.1
elif assinatura == "PLATINUM":
    porcentagem = 0.05
else:
    porcentagem = 0

# Verifica o valor da variável porcentagem para realizar o cálculo do bônus, e lança o output do mesmo ou
# se o usuário digitou um opção inválida:
if porcentagem != 0:
    bonus = faturamento_anual * porcentagem
    print(f"\nO valor do bônus é R$ {bonus:.2f}.")
else:
    print("\nAssinatura inválida!")
