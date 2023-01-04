num = int(input('Digite um número inteiro: '))

print('\nEscolha uma das bases para conversão:'
      '\n[ 1 ] converter para BINÁRIO'
      '\n[ 2 ] converter para OCTAL'
      '\n[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'\n{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
elif opcao == 2:
    print(f'\n{num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif opcao == 3:
    print(f'\n{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print(f'\nA opção "{opcao}" é inválida. Tente novamente.')
