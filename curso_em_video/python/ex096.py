def area(l, c):
    total = l * c
    print(f"A área de um terreno {l} x {c} é de {total} m².")


largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))

area(largura, comprimento)
