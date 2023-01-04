def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + ((preco * taxa) / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - ((preco * taxa) / 100)
    return res if formato is False else moeda(res)


def moeda(preco=0, monet="R$"):
    return f"{monet} {preco:>.2f}".replace(".", ",")
