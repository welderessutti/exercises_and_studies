num = int(input('Digite o número da tabuada: '))

for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')

# ABAIXO UMA TABUADA QUE PODE ESCOLHER ATÉ ONDE ELA ACABA.

num = int(input('Digite o número da tabuada: '))
num_final = int(input('Até quanto?: '))

for c in range(1, num_final + 1):
    print(f'{num} x {c} = {num * c}')
