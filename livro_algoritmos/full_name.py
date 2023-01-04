first_name = 'Welder'
second_name = 'Ressutti'
full_name = first_name + second_name
age = 33

print(full_name)

print('Olá ' + full_name + ' ' + str(age) + ' anos')
print('Olá', full_name, age, 'anos')
print('Olá {} {} anos' .format(full_name, age))
print(f'Olá {full_name} {age} anos')

# ERRADO (É "STRING" POIS NÃO ESTÁ DECLADA NO INÍCIO DO "INPUT"!)
n1 = input('digite um núemro: ')
n2 = input('digite um núemro: ')
n3 = n1 + n2

print(int(n1) + int(n2))
print(n3)
print(type(n3))

# CORRETO
n4 = int(input('digite um número: '))
n5 = int(input('digite um número: '))
n6 = n4 + n5

print(n6)
print(type(n6))
