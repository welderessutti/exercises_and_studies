# Litros gastos na viagem
# autonomia 12 Km por litro

tempo = float(input("Digite o tempo gasto total de horas da viagem: "))
velocidade = float(input("Digite a velocidade média da viagem: "))

distancia = tempo * velocidade
litros = distancia / 12

print(f"A velociadade média da viagem foi de {velocidade} Km/h, o tempo gasto da viagem foi de {tempo} h, a distância percorrida foi de {distancia} Km e a quantidade de combustível consumido foi de {litros} L.")
