# ORDEM PRECEDÊNCIA
# ()
# **
# * / // %
# - +
# raiz quadrada x**(1/2)
# raiz cubica x**(1/3)

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
exp = n1 ** n2
div_int = n1 // n2
div_rest = n1 % n2

print(f'\nSoma = {s}\nSubtração = {sub}\nMultiplicação = {m}\nDivisão = {d}\nExponenciação = {exp}\nDivisão Inteira = {div_int}\nResto Divisão = {div_rest}')
