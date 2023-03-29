segunda = int(input("Votos para Segunda-Feira: "))
terca = int(input("Votos para Terça-Feira: "))
quarta = int(input("Votos para Quarta-Feira: "))
quinta = int(input("Votos para Quinta-Feira: "))
sexta = int(input("Votos para Sexta-Feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    dia_escolhido = "Segunda-Feira"
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    dia_escolhido = "Terça-Feira"
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    dia_escolhido = "Quarta-Feira"
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    dia_escolhido = "Quinta-Feira"
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    dia_escolhido = "Sexta-Feira"
else:
    dia_escolhido = "empate"

if dia_escolhido != "empate":
    print(f"\nO dia escolhido foi {dia_escolhido}.")
else:
    print(f"\nDeu {dia_escolhido}!")
