from ex_111_112 import moeda
from ex_111_112 import dado

p = dado.leia_dinheiro("Digite o preço: R$ ")
moeda.resumo(p, 35, 22)

p = dado.leia_dinheiro_1("Digite o preço: R$ ")
moeda.resumo(p, 35, 22)
