from collections import defaultdict, Counter

aparicoes = {"Welder": 1, "cachorro": 2, "nome": 2, "vindo": 1}
print(aparicoes)

print(aparicoes.get("xpto", 0))  # Retorna a quantidade de apariçôes do valor pesquisado, caso não exista, retorna zero.
print(aparicoes.get("cachorro", 0))

aparicoes = dict(Welder=2, cachorro=1, nome=2, vindo=1)  # Outra forma de declarar um dicionário com o construtor dict().
print(aparicoes)
print()

meu_texto = "Bem vindo meu nome é Welder eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():  # Conta quantas vezes aparece a palavra no texto.
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)

aparicoes = defaultdict(int)

for palavra in meu_texto.split():  # Mesma coisa de cima utilizando o defaultdict().
    aparicoes[palavra] += 1
print(aparicoes)

aparicoes = Counter(meu_texto.split())  # Mesma coisa de cima utilizando o Counter().
print(aparicoes)
