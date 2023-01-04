num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'O número contém {len(str(num))} dígitos.')
print(f'Unidade do número é {u}.')
print(f'Dezena do número é {d}')
print(f'Centena do número é {c}')
print(f'Milhar do número é {m}')
