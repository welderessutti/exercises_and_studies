# DESSE JEITO QUE EU FIZ ELE DÁ ERRO (TRACEBACK) QUANDO DIGITA SOMENTE VÍRGULA OU PONTO:
def leia_dinheiro(valor):
    while True:
        res = input(valor).replace(",", ".").strip()
        if res.isalpha() or res == "":
            print(f'ERRO: "{res}" é um preço inválido!')
        else:
            res = float(res)
            break
    return res


# UMA FORMA COMPLETA PODENDO DIGITAR VÍRGULA E PONTO QUE POSTARAM NOS COMENTÁRIOS:
def leia_dinheiro_1(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.count('.') == 1 and len(entrada) > 1 and entrada.find('.') != 0 and entrada.replace('.', '0').isnumeric():
            valido = True
            return float(entrada)
        elif entrada.isnumeric():
            valido = True
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
