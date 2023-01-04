def computador_escolhe_jogada(n, m):
    cont = 1
    jogada = m
    while cont <= m:
        resto = n - jogada
        if resto % (m + 1) == 0:
            return jogada
        else:
            jogada -= 1
            cont += 1
    return m


def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            break
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")
    return jogada


def partida():
    while True:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogadas? "))
        if n > 0 and 0 < m <= n:
            break
        else:
            print("\nOpção inválida!\n")
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        while n > 0:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            if jogada_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print(f"Você tirou {jogada_usuario} peças.")
            if n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            elif n == 1:
                print(f"Agora resta apenas uma peça no tabuleiro.\n")
            elif n == 0:
                print("Fim do jogo! Você ganhou!\n")
                return False
            jogada_computador = computador_escolhe_jogada(n, m)
            n -= jogada_computador
            if jogada_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {jogada_computador} peças.")
            if n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            elif n == 1:
                print(f"Agora resta apenas uma peça no tabuleiro.\n")
            elif n == 0:
                print("Fim do jogo! O computador ganhou!\n")
                return True
    else:
        print("\nComputador começa!\n")
        while n > 0:
            jogada_computador = computador_escolhe_jogada(n, m)
            n -= jogada_computador
            if jogada_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {jogada_computador} peças.")
            if n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            elif n == 1:
                print(f"Agora resta apenas uma peça no tabuleiro.\n")
            elif n == 0:
                print("Fim do jogo! O computador ganhou!\n")
                return True
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            if jogada_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print(f"Você tirou {jogada_usuario} peças.")
            if n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            elif n == 1:
                print(f"Agora resta apenas uma peça no tabuleiro.\n")
            elif n == 0:
                print("Fim do jogo! Você ganhou!\n")
                return False


def campeonato():
    rodadas = 1
    pontos_computador = 0
    pontos_usuario = 0
    while rodadas <= 3:
        print(f"**** Rodada {rodadas} ****\n")
        if partida():
            pontos_computador += 1
        else:
            pontos_usuario += 1
        rodadas += 1
    print("**** Final do Campeonato ****\n")
    print(f"Placar: Você {pontos_usuario} X {pontos_computador} Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    while True:
        opcao = int(input("1 - para jogar uma partida isolada\n"
                          "2 - para jogar um campeonato "))
        if 1 <= opcao <= 2:
            break
        else:
            print("\nOpção inválida!\n")
    if opcao == 1:
        print("\nVoce escolheu partida isolada!\n")
        partida()
    elif opcao == 2:
        print("\nVoce escolheu um campeonato!\n")
        campeonato()


main()
