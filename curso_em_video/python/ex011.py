largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
litros_tinta = area / 2

print(f'Para pintar a parede será necessário {litros_tinta} litros de tinta.')
