ht = float(input("Digite o seu total de horas trabalhadas no mês: "))
vh = float(input("Digite o valor da sua hora-aula: "))
pd = float(input("Digite o valor do seu percentual de desconto: "))

# ht = 220
# vh = 40
# pd = 25

sb = ht * vh
td = (pd / 100) * sb
sl = sb - td

print(f"\n\tO salário bruto do professor é de: R$ {sb}.")
print(f"\tO salário líquido do professor é de: R$ {sl}.")
