velocidade = float(input('Digite a velocidade: '))

if velocidade > 80:
    print(f'\033[1:31mMULTADO!\033[m Vocẽ ultrapassou o limite de velocidade que é de 80 Km/h. Velocidade registrada {velocidade} Km/h. Valor da multa R$ {(velocidade - 80) * 7:.2f}.')
else:
    print('Boa viagem! Tenha um bom dia, dirija com segurança.')
