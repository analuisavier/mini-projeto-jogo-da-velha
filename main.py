import numpy as np
import time
import os

# Códigos de escape ANSI para cores
CORES = {
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',
    'italico': '\033[3m',
    'reset': '\033[0m'
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

COR_X = CORES['roxo']  
COR_O = CORES['ciano']  

def exibir_x():
    return f"{COR_X}X{CORES['reset']}"

def exibir_o():
    return f"{COR_O}O{CORES['reset']}"

#Variáveis
jogador_X = "Jogador X"
jogador_O = "Jogador O"
tamanho_tabuleiro = 3
tamanho_sequencia = 3
placar = {}

# FUNÇÕES DE LÓGICA DO JOGO 

def criar_tabuleiro(tamanho):
    #Cria uma matriz vazia para o tabuleiro.
    return np.full((tamanho, tamanho), ' ')

def exibir_tabuleiro(tabuleiro):
    # Exibe o tabuleiro formatado com coordenadas.
    limpar_tela()
    tamanho = len(tabuleiro)
    
    print("   " + "   ".join([f"{CORES['amarelo']}{i}{CORES['reset']}" for i in range(tamanho)]))
    
    print("  " + "---" * tamanho + "-" * (tamanho - 1))

    for i in range(tamanho):
        # Imprime a letra da linha (A a J)
        print(f"{CORES['amarelo']}{chr(ord('A') + i)}{CORES['reset']}{CORES['branco']}|{CORES['reset']}", end="")
        for j in range(tamanho):
            if tabuleiro[i, j] == 'X':
                print(f" {exibir_x()} ", end="")
            elif tabuleiro[i, j] == 'O':
                print(f" {exibir_o()} ", end="")
            else:
                print("   ", end="")
            if j < tamanho - 1:
                print(f"{CORES['branco']}|{CORES['reset']}", end="")
        print(f"{CORES['branco']}|{CORES['reset']}")
        if i < tamanho - 1:
            print("  " + "---" * tamanho + "-" * (tamanho - 1))
    
    print("  " + "---" * tamanho + "-" * (tamanho - 1))
    
def verificar_vitoria(tabuleiro, jogador_simbolo, linha, coluna, sequencia_vitoria):
    tamanho = len(tabuleiro)

    # Função auxiliar para contar a sequência em uma direção
    def contar_sequencia(dx, dy):
        count = 0
        # Conta em uma direção 
        for i in range(1, sequencia_vitoria):
            x, y = linha + i * dx, coluna + i * dy
            if 0 <= x < tamanho and 0 <= y < tamanho and tabuleiro[x, y] == jogador_simbolo:
                count += 1
            else:
                break
        # Conta na direção oposta (ex: para a esquerda)
        for i in range(1, sequencia_vitoria):
            x, y = linha - i * dx, coluna - i * dy
            if 0 <= x < tamanho and 0 <= y < tamanho and tabuleiro[x, y] == jogador_simbolo:
                count += 1
            else:
                break
        return count + 1 # +1 para contar a peça jogada

    # Verifica horizontal, vertical e as duas diagonais
    direcoes = [(0, 1), (1, 0), (1, 1), (1, -1)] # Horizontal, Vertical, Diagonal Principal, Diagonal Secundária
    for dx, dy in direcoes:
        if contar_sequencia(dx, dy) >= sequencia_vitoria:
            return True
    return False

def partida():
    tabuleiro = criar_tabuleiro(tamanho_tabuleiro)
    jogador_atual_nome = jogador_X
    jogador_atual_simbolo = 'X'
    total_jogadas = 0

    while total_jogadas < tamanho_tabuleiro ** 2:
        exibir_tabuleiro(tabuleiro)
        
        if jogador_atual_simbolo == 'X':
            print(f"\nÉ a vez de {exibir_x()} ({jogador_atual_nome})")
        else:
            print(f"\nÉ a vez de {exibir_o()} ({jogador_atual_nome})")

        try:
            jogada_str = input("Digite a sua jogada no formato 'linha coluna' (ex: a 0): ")
            jogada_split = jogada_str.split()
            
            if len(jogada_split) != 2:
                raise ValueError("Entrada inválida. Digite uma letra e um número.")

            letra_linha = jogada_split[0].lower()
            # Converte a letra da linha para um índice numérico (A=0, B=1, etc.)
            linha = ord(letra_linha) - ord('A')
            coluna = int(jogada_split[1])

            if not (0 <= linha < tamanho_tabuleiro and 0 <= coluna < tamanho_tabuleiro):
                print(f"{CORES['vermelho']}Jogada fora do tabuleiro! Tente novamente.{CORES['reset']}")
                time.sleep(1.5)
                continue
            
            if tabuleiro[linha, coluna] != ' ':
                print(f"{CORES['vermelho']}Esta posição já está ocupada! Tente novamente.{CORES['reset']}")
                time.sleep(1.5)
                continue

        except (ValueError, IndexError):
            print(f"{CORES['vermelho']}Entrada inválida. Use o formato 'letra número' (ex: a 0) com coordenadas válidas.{CORES['reset']}")
            time.sleep(2)
            continue
        
        # Realiza a jogada
        tabuleiro[linha, coluna] = jogador_atual_simbolo
        total_jogadas += 1

        # Verifica se houve um vencedor
        if verificar_vitoria(tabuleiro, jogador_atual_simbolo, linha, coluna, tamanho_sequencia):
            exibir_tabuleiro(tabuleiro)
            return jogador_atual_nome

        # Troca de jogador
        if jogador_atual_simbolo == 'X':
            jogador_atual_nome = jogador_O
            jogador_atual_simbolo = 'O'
        else:
            jogador_atual_nome = jogador_X
            jogador_atual_simbolo = 'X'
    
    exibir_tabuleiro(tabuleiro)
    return None # Retorna None em caso de empate

# FUNÇÕES DO MENU 
def mostrar_placar(placar_atual):
    print(f"\n{CORES['amarelo']}Placar:{CORES['reset']}")
    if not placar_atual:
        print("O placar ainda está vazio.")
    else:
        # Garante que os jogadores atuais estejam no placar para exibição
        if jogador_X not in placar_atual: placar_atual[jogador_X] = 0
        if jogador_O not in placar_atual: placar_atual[jogador_O] = 0

        # Itera sobre os itens para ver o nome e os pontos
        for jogador, pontos in placar_atual.items():
            if jogador == jogador_X:
                print(f"{exibir_x()} {CORES['verde']}{jogador}: {pontos}{CORES['reset']}")
            elif jogador == jogador_O:
                print(f"{exibir_o()} {CORES['verde']}{jogador}: {pontos}{CORES['reset']}")
        
        # Remove jogadores do placar se eles não forem mais os jogadores X ou O atuais
        jogadores_para_remover = [j for j in placar_atual if j not in [jogador_X, jogador_O]]
        for j in jogadores_para_remover:
            del placar_atual[j]


# LOOP PRINCIPAL MENU 
while True:
    limpar_tela()
    
    print(f"\n{CORES['amarelo']}Menu Principal - Jogo da Velha{CORES['reset']}")
    print(f"1. Definir nome do jogador {exibir_x()} (Atual: {jogador_X})")
    print(f"2. Definir nome do jogador {exibir_o()} (Atual: {jogador_O})")
    print(f"3. Definir tamanho do tabuleiro (Atual: {tamanho_tabuleiro}x{tamanho_tabuleiro})")
    print(f"4. Definir sequência para vitória (Atual: {tamanho_sequencia})")
    print("5. Mostrar placar")
    print("6. Iniciar novo jogo")
    print("7. Sair do jogo")
    time.sleep(0.5)

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        novo_nome_x = input("Digite o nome do jogador X: ")
        if novo_nome_x: 
            placar[novo_nome_x] = placar.pop(jogador_X, 0)
            jogador_X = novo_nome_x
        time.sleep(1.5)
            
    elif opcao == '2':
        novo_nome_o = input("Digite o nome do jogador O: ")
        if novo_nome_o:
            placar[novo_nome_o] = placar.pop(jogador_O, 0)
            jogador_O = novo_nome_o
        time.sleep(1.5)
            
    elif opcao == '3':
        try:
            novo_tamanho = int(input(f"Digite o tamanho do tabuleiro (entre 3 e 10): "))
            if 3 <= novo_tamanho <= 10:
                tamanho_tabuleiro = novo_tamanho
                print(f"{CORES['verde']}Tamanho do tabuleiro definido: {tamanho_tabuleiro}x{tamanho_tabuleiro}{CORES['reset']}")
                if tamanho_sequencia > tamanho_tabuleiro:
                    tamanho_sequencia = tamanho_tabuleiro
                    print(f"{CORES['amarelo']}Sequência de vitória ajustada para {tamanho_sequencia}{CORES['reset']}")
            else:
                print(f"{CORES['vermelho']}Tamanho deve estar entre 3 e 10!{CORES['reset']}")
        except ValueError:
            print(f"{CORES['vermelho']}Por favor, digite um número válido!{CORES['reset']}")
        time.sleep(1.5)
        
    elif opcao == '4':
        try:
            nova_sequencia = int(input(f"Digite o tamanho da sequência para vitória: "))
            if 3 <= nova_sequencia <= tamanho_tabuleiro:
                tamanho_sequencia = nova_sequencia
                print(f"{CORES['verde']}Sequência para vitória definida: {tamanho_sequencia}{CORES['reset']}")
            else:
                print(f"{CORES['vermelho']}Sequência deve estar entre 3 e {tamanho_tabuleiro}!{CORES['reset']}")
        except ValueError:
            print(f"{CORES['vermelho']}Por favor, digite um número válido!{CORES['reset']}")
        time.sleep(1.5)
        
    elif opcao == '5':
        mostrar_placar(placar)
        input("\nPressione Enter para continuar...")
    
    elif opcao == '6':
        limpar_tela()
        print(f"\n{CORES['ciano']}Iniciando novo jogo...{CORES['reset']}")
        time.sleep(1)
        
        if jogador_X not in placar: placar[jogador_X] = 0
        if jogador_O not in placar: placar[jogador_O] = 0
            
        print(f"Jogador {exibir_x()}: {jogador_X}")
        print(f"Jogador {exibir_o()}: {jogador_O}")
        print(f"Tabuleiro: {tamanho_tabuleiro}x{tamanho_tabuleiro}")
        print(f"Sequência para vitória: {tamanho_sequencia}")
        time.sleep(5)

        vencedor_da_partida = partida()

        if vencedor_da_partida:
            placar[vencedor_da_partida] += 1
            if vencedor_da_partida == jogador_X:
                print(f"\n{CORES['verde']}{exibir_x()} {vencedor_da_partida} venceu!{CORES['reset']}")
            else:
                print(f"\n{CORES['verde']}{exibir_o()} {vencedor_da_partida} venceu!{CORES['reset']}")
        else:
            print(f"\n{CORES['amarelo']}O jogo terminou em empate!{CORES['reset']}")

        time.sleep(2)
        print(f"\n{CORES['azul']}Retornando ao menu...{CORES['reset']}")
        input("Pressione Enter para continuar...")

    elif opcao == '7':
        limpar_tela()
        print(f"{CORES['vermelho']}Saindo do jogo. Até mais!{CORES['reset']}")
        time.sleep(1)
        break
    
    else:
        print(f"{CORES['vermelho']} Opção inválida! Por favor, escolha uma opção de 1 a 7.{CORES['reset']}")
        time.sleep(1.5)