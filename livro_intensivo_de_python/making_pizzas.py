import module_pizza
import module_pizza as p
from module_pizza import make_pizza
from module_pizza import make_pizza as mp
from module_pizza import *  # * IMPORTA TODAS AS FUNÇÕES DO MÓDULO SEM PRECISAR USAR A NOTAÇÃO DE PONTO.
# MAS NÃO É RECOMENDADO USAR ESSE TIPO DE IMPORTAÇÃO POIS PODE GERAR CONFLITO COM NOMES DE OUTRAS FUNÇÕES.

module_pizza.make_pizza(16, "pepperoni")
module_pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")
