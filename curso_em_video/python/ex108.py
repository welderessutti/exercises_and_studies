from ex_108 import moeda_format

p = float(input(f"Digite o preço: R$ "))
print(f"A metade de {moeda_format.moeda(p)} é {moeda_format.moeda(moeda_format.metade(p))}.")
print(f"O dobro de {moeda_format.moeda(p)} é {moeda_format.moeda(moeda_format.dobro(p))}.")
print(f"Aumentando 10% temos {moeda_format.moeda(moeda_format.aumentar(p, 10))}.")
print(f"Reduzindo 13% temos {moeda_format.moeda(moeda_format.diminuir(p, 13))}.")
