print("\n=== Jogo de Dados ===")

import random

def jogar_dados():
    """Simula o lançamento de dois dados"""
    
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Soma: {soma}")
    
    # Verificações usando operadores aritméticos
    if soma % 2 == 0:
        print("Soma é par!")
    else:
        print("Soma é ímpar!")
    
    if soma == 7:
        print("🎉 Sorte! Soma 7!")
    elif soma == 12:
        print("🎆 Jackpot! Soma máxima!")
    elif soma == 2:
        print("😅 Azar! Soma mínima!")

# Jogar 3 vezes
for rodada in range(1, 4):
    print(f"\nRodada {rodada}:")
    jogar_dados()
