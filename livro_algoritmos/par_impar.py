num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O número \033[0;34m{num}\033[m é \033[0;34mPAR!\033[m')
else:
    print(f'O número \033[0;31m{num}\033[m é \033[0;31mÍMPAR!\033[m')
