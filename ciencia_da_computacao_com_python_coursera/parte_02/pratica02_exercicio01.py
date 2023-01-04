def conta_letras(frase, contar="vogais"):
    vog_list = ["a", "e", "i", "o", "u"]
    pos = 0
    cont_vog = 0
    cont_cons = 0
    while pos < len(frase):
        if frase[pos].lower() in vog_list:
            cont_vog += 1
        elif frase[pos].lower() not in vog_list and frase[pos] != " ":
            cont_cons += 1
        pos += 1
    if contar == "consoantes":
        return cont_cons
    else:
        return cont_vog
