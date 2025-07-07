import numpy as np
import time
import os

# Códigos de escape ANSI
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

COR_X = CORES['roxo']     #cor para o X
COR_O = CORES['ciano']     #cor para o O

def exibir_x():
    return f"{COR_X}X{CORES['reset']}"

def exibir_o():
    return f"{COR_O}O{CORES['reset']}"

jogador_X = "Jogador X"
jogador_O = "Jogador O"
tamanho_tabuleiro = 3
tamanho_sequencia = 3
placar = {} 

def mostrar_placar(placar_atual):
    print(f"\n{CORES['amarelo']}Placar:{CORES['reset']}")
    if not placar_atual:
        print("O placar ainda está vazio.")
    else:
        # Itera sobre os itens para ver o nome e os pontos
        for jogador, pontos in placar_atual.items():
            if jogador == jogador_X:
                print(f"{exibir_x()} {CORES['verde']}{jogador}: {pontos}{CORES['reset']}")
            elif jogador == jogador_O:
                print(f"{exibir_o()} {CORES['verde']}{jogador}: {pontos}{CORES['reset']}")
            else:
                print(f"{CORES['verde']}{jogador}: {pontos}{CORES['reset']}")

while True:
    limpar_tela()
    
    print(f"\n{CORES['amarelo']}Menu:{CORES['reset']}")
    print(f"1. Definir jogador {exibir_x()}")
    print(f"2. Definir jogador {exibir_o()}")
    print("3. Definir tamanho do tabuleiro")
    print("4. Definir tamanho da sequência")
    print("5. Mostrar placar")
    print("6. Iniciar novo jogo")
    print("7. Sair do jogo")
    time.sleep(0.5)

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        jogador_X = input("Digite o nome do jogador X: ")
        # Inicializa o placar para o jogador X
        if jogador_X not in placar:
            placar[jogador_X] = 0
        time.sleep(1.5)
            
    elif opcao == '2':
        jogador_O = input("Digite o nome do jogador O: ")
        # Inicializa o placar para o jogador O 
        if jogador_O not in placar:
            placar[jogador_O] = 0
        time.sleep(1.5)
        
            
    elif opcao == '3':
        try:
            novo_tamanho = int(input("Digite o tamanho do tabuleiro: "))
            if novo_tamanho >= 3:
                tamanho_tabuleiro = novo_tamanho
                print(f"{CORES['verde']}Tamanho do tabuleiro definido: {tamanho_tabuleiro}x{tamanho_tabuleiro}{CORES['reset']}")
            else:
                print(f"{CORES['vermelho']}Tamanho deve ser no mínimo 3!{CORES['reset']}")
        except ValueError:
            print(f"{CORES['vermelho']}Por favor, digite um número válido!{CORES['reset']}")
        time.sleep(1.5)
        
    elif opcao == '4':
        try:
            nova_sequencia = int(input("Digite o tamanho da sequência para vitória: "))
            if 3 <= nova_sequencia <= tamanho_tabuleiro:
                tamanho_sequencia = nova_sequencia
                print(f"{CORES['verde']}Sequência para vitória definida: {tamanho_sequencia}{CORES['reset']}")
            else:
                print(f"{CORES['vermelho']}Sequência deve estar entre 3 e {tamanho_tabuleiro}!{CORES['reset']}")
        except ValueError:
            print(f"{CORES['vermelho']}Por favor, digite um número válido!{CORES['reset']}")
        time.sleep(1.5)
        
    elif opcao == '5':
        # Chama a função para mostrar o placar
        mostrar_placar(placar)
        input("Pressione Enter para continuar...")
    
    elif opcao == '6':
        print(f"\n{CORES['ciano']}Iniciando novo jogo...{CORES['reset']}")
        time.sleep(1)
        
        print(f"Jogador {exibir_x()}: {jogador_X}")
        print(f"Jogador {exibir_o()}: {jogador_O}")
        print(f"Tabuleiro: {tamanho_tabuleiro}x{tamanho_tabuleiro}")
        print(f"Sequência para vitória: {tamanho_sequencia}")
        time.sleep(2)
        
        vencedor_da_partida = jogador_X  # para testar 

        if vencedor_da_partida and vencedor_da_partida in placar:
            placar[vencedor_da_partida] += 1
            if vencedor_da_partida == jogador_X:
                print(f"\n{CORES['verde']}{exibir_x()} {vencedor_da_partida} venceu!{CORES['reset']}")
            else:
                print(f"\n{CORES['verde']}{exibir_o()} {vencedor_da_partida} venceu!{CORES['reset']}")
        else:
            # caso de empate
            print(f"\n{CORES['amarelo']}O jogo terminou em empate!{CORES['reset']}")

        time.sleep(2)
        print(f"{CORES['azul']}Retornando ao menu...{CORES['reset']}")
        input("Pressione Enter para continuar...")

    elif opcao == '7':
        limpar_tela()
        print(f"{CORES['vermelho']}Saindo do jogo. Até mais!{CORES['reset']}")
        time.sleep(1)
        break
    
    else:
        print(f"{CORES['vermelho']} Opção inválida! Por favor, escolha uma opção de 1 a 7.{CORES['reset']}")
        time.sleep(1.5)