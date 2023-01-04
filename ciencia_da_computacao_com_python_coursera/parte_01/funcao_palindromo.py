def palindromo(palavra):
    letra = 0
    while letra < len(palavra):
        if palavra[letra] != palavra[len(palavra) - letra - 1]:
            return False
        letra = letra + 1
    return True


print(palindromo("ama"))
