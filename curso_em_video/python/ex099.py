from time import sleep


def maior(*num):
    maior_1 = cont = 0
    print("=-" * 20)
    print("Analisando os valores passados...")
    for c in num:
        print(f"{c}", end=" ")
        sleep(0.5)
        if cont == 0:
            maior_1 = c
        else:
            if c > maior_1:
                maior_1 = c
        cont += 1
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {maior_1}.")


maior(-1, 2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(-1)
maior()
