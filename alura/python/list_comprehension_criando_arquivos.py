print("R$ {:7.1f}".format(1000.12))
print("R$ {:07.2f}".format(4.11))

print(round(11/3))

'''while True:
    a = int(input("a: "))
    if a == 1:
        print(a)
        continue
    print(2)'''

inteiros = [1, 3, 4, 5, 7, 8, 9]

pares = [numero for numero in inteiros if numero % 2 == 0]

print(pares)

arquivo = open("frutas", "w")

arquivo.write("maçã\n")
arquivo.write("goiaba\n")
arquivo.write("laranja\n")
arquivo.write("abacate\n")

arquivo.close()
