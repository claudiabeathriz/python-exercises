def exibir_tabuleiro(tabuleiro):

    print("\nTABULEIRO:\n")

    # cabeçalho das colunas
    print("    0   1   2")
    print("  -------------")

    # percorre as linhas
    for i in range(len(tabuleiro)):

        # exibe o número da linha
        print(f"{i} ", end="")

        # percorre as colunas da linha atual
        for j in range(len(tabuleiro[i])):

            print(f"| {tabuleiro[i][j]} ", end="")

        print("|")
        print("  -------------")

def verificar_vitoria(tabuleiro, jogador):

    # tabuleiro -> [linha][coluna]
    # verifica as 3 linhas; mantém a linha fixa e muda a coluna
    # quando i = 0, olha toda a primeira linha
    # quando i = 1, olha toda a segunda linha
    # quando i = 2, olha toda a terceira linha
    for i in range(3):

        if (
            tabuleiro[i][0] == jogador and
            tabuleiro[i][1] == jogador and
            tabuleiro[i][2] == jogador
        ):
            return True

    # verifica as 3 colunas; agora coluna fica fixa e linha muda
    # quando i = 0, olha toda a primeira coluna
    # quando i = 1, olha toda a segunda coluna
    # quando i = 2, olha toda a terceira coluna
    for i in range(3):

        if (
            tabuleiro[0][i] == jogador and
            tabuleiro[1][i] == jogador and
            tabuleiro[2][i] == jogador
        ):
            return True

    # verifica a diagonal principal
    # exemplo:
    # X |   | -> [0][0]
    #   | X | -> [1][1]
    #   |   | X -> [2][2]
    if (
        tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador
    ):
        return True

    # verifica a diagonal secundária
    # exemplo:
    #   |   | X -> [0][2]
    #   | X | -> [1][1]
    # X |   | -> [2][0]
    if (
        tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador
    ):
        return True

    # caso nenhuma condição seja atendida:
    return False

def jogada_valida(tabuleiro, linha, coluna):

    # verifica se a linha está dentro dos limites da matriz
    if linha < 0 or linha > 2:
        return False

    # verifica se a coluna está dentro dos limites da matriz
    if coluna < 0 or coluna > 2:
        return False

    # verifica se a posição escolhida está vazia
    if tabuleiro[linha][coluna] != " ":
        return False

    return True

# ==========================
# PROGRAMA PRINCIPAL
# ==========================

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# jogador X sempre começa
jogador = "X"

# contador de jogadas
jogadas = 0

# variável que indica se alguém venceu
# sempre começa falso, pois ainda não há vencedor
vencedor = False

# o jogo continua enquanto não houver vencedor e ainda existirem posições livres
while not vencedor and jogadas < 9:

    # mostra o estado atual do tabuleiro
    exibir_tabuleiro(tabuleiro)

    print(f"\nVez do jogador {jogador}")

    # recebe a posição desejada
    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna (0, 1 ou 2): "))

    # verifica se a jogada é válida
    if not jogada_valida(tabuleiro, linha, coluna):

        print("Jogada inválida!")
        continue

    # coloca o símbolo do jogador na posição escolhida
    tabuleiro[linha][coluna] = jogador

    # incrementa o contador de jogadas
    jogadas += 1

    # verifica se o jogador venceu
    if verificar_vitoria(tabuleiro, jogador):

       vencedor = True

    else:

        # troca o jogador
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"

# exibe o tabuleiro final
exibir_tabuleiro(tabuleiro)

# mostra o resultado da partida
if vencedor:
    print(f"O jogador {jogador} venceu!")
else:
    print("O jogo terminou em empate!")