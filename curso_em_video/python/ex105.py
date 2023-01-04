def notas(*num, sit=False):
    """

    :param num: Recebe várias notas
    :param sit: (Opcional) Se True, mostra a situação.
    :return: Retorna total, maior, menor, média e situação.
    """
    boletim = {}
    maior = menor = soma = media = cont = 0
    for c in num:
        if cont == 0 or c > maior:
            maior = c
        if cont == 0 or c < menor:
            menor = c
        cont += 1
        soma += c
        media = soma / cont
    boletim["total"] = cont
    boletim["maior"] = maior
    boletim["menor"] = menor
    boletim["média"] = media

    if sit:
        if media < 5:
            boletim["situação"] = "RUIM"
        elif 5 <= media < 7:
            boletim["situação"] = "RAZOÁVEL"
        elif 7 <= media:
            boletim["situação"] = "BOA"
    return boletim


resp = notas(5.5, 3.5, 10, 6.5, 8.0, sit=True)
print(resp)

# PROFESSOR FEZ USANDO FUNÇÕES LOCAIS:


def notas_1(*n, sit=False):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n) / len(n)
    if sit:
        if r["média"] >= 7:
            r["situação"] = "BOA"
        elif r["média"] >= 5:
            r["situação"] = "RAZOÁVEL"
        else:
            r["situação"] = "RUIM"
    return r


resp_1 = notas_1(5.5, 3.5, 10, 6.5, 8.0, sit=True)
print(resp_1)
