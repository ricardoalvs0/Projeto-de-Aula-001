def usuario_escolhe_jogada(n, m):
    i = 0
    while i != 1:
        novoN = int(input('Quantas peças você vai tirar? '))
        if novoN > m or novoN > n or novoN == 0:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            i = 1
            if novoN == 1:
                print(f'\nVocê tirou uma peça.')
            else:
                print(f'\nVocê tirou {novoN} peças.')
    return novoN


def computador_escolhe_jogada(n, m):
    novo_n = 1
    jogadacerta = False
    if n == 0:
        return 0
    while (novo_n < m and novo_n < n) and not jogadacerta:
        if (n - novo_n) % (m + 1) == 0:
            jogadacerta = True
        else:
            novo_n += 1
    if novo_n == 1:
        print(f'O computador tirou uma peça.')
    else:
        print(f'O computador tirou {novo_n} peças.')
    return novo_n


def partida():
    valido = False
    while not valido:
        n = input('Quantas peças? ')
        m = input('Limite de peças por jogadas? ')
        if n.isnumeric() and m.isnumeric():
            if int(n) < int(m) or int(m) == 0:
                print(
                    '\nInválido! O número de peças no tabuleiro deve ser maior que o máximo de peças a serem retiradas!')
                print('O número de peças a serem retiradas deve ser maior que 0!\n')
            else:
                valido = True
                n = int(n)
                m = int(m)
        else:
            print('Inválido! Digite um número!\n')
        x = 0
        y = 0
    if n % (m + 1) == 0:

        print('\nVocê começa!')
        while n > 0:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if n != 0:
                if n == 1:
                    print(f'Agora resta uma peça no tabuleiro.\n')
                else:
                    print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Fim do jogo! O jogador ganhou!')
                y += 1
                break
            jogadapc = computador_escolhe_jogada(n, m)
            n -= jogadapc
            if n != 0:
                if n == 1:
                    print(f'Agora resta uma peça no tabuleiro.\n')
                else:
                    print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('\nFim do jogo! O computador ganhou!')
                x += 1
                break
    else:
        print('\nComputador começa!\n')
        while n > 0:
            jogadapc = computador_escolhe_jogada(n, m)
            n -= jogadapc
            if n != 0:
                if n == 1:
                    print(f'Agora resta uma peça no tabuleiro.\n')
                else:
                    print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Fim do jogo! O computador ganhou!')  # Falta O Placar
                x += 1
                break
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if n != 0:
                if n == 1:
                    print(f'Agora resta uma peça no tabuleiro.\n')
                else:
                    print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Fim do jogo! O jogador ganhou!')
                y += 1
                break
    return x, y


def main():
    validade = False
    while not validade:
        escolha = int(input(
            'Bem vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
        i = 1
        pc = 0
        usu = 0
        if escolha == 1:
            partida()
            validade = True
        elif escolha == 2:
            validade = True
            print('\nVocê escolheu um campeonato!')
            while i <= 3:
                print(f'\n**** Rodada {i} ****\n')
                x = partida()
                pc += x[0]
                usu += x[1]
                i += 1
            print('\n**** Final do campeonato! ****\n')
            print(f'Placar: Você {usu} X {pc} Computador')
        # placar()
        else:
            print('Escolha inválida!\n')


main()
#usuario_escolhe_jogada(6,4)
#computador_escolhe_jogada(13, 4)
