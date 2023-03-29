assinatura = input("Tipo de assinatura: ").strip().upper()
faturamento_anual = float(input("Faturamento anual: "))

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

if porcentagem != 0:
    bonus = faturamento_anual * porcentagem
    print(f"\nO valor do bônus é R$ {bonus:.2f}.")
else:
    print("\nAssinatura inválida!")
