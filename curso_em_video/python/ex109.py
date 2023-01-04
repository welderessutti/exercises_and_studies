from ex_109 import moeda_parametro

p = float(input(f"Digite o preço: R$ "))
print(f"A metade de {moeda_parametro.moeda(p)} é {moeda_parametro.metade(p, True)}.")
print(f"O dobro de {moeda_parametro.moeda(p)} é {moeda_parametro.dobro(p, True)}.")
print(f"Aumentando 10% temos {moeda_parametro.aumentar(p, 10, True)}.")
print(f"Reduzindo 13% temos {moeda_parametro.diminuir(p, 13, True)}.")
