dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))
cont_int = 1

resto = dividendo - divisor

while resto >= divisor:
    dividendo = resto
    resto = dividendo - divisor
    cont_int += 1

print(cont_int)
