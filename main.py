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