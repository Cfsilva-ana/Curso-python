print("=== Jogo de Adivinhação ===")

import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 7

print("🎮 Jogo de Adivinhação!")
print(f"Adivinhe o número entre 1 e 100 (você tem {max_tentativas} tentativas)")

while tentativas < max_tentativas:
    try:
        palpite = int(input(f"\nTentativa {tentativas + 1}: "))
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("📈 Muito baixo! Tente um número maior.")
        else:
            print("📉 Muito alto! Tente um número menor.")
        
        # Mostrar tentativas restantes
        restantes = max_tentativas - tentativas
        if restantes > 0:
            print(f"Tentativas restantes: {restantes}")
        
    except ValueError:
        print("❌ Digite apenas números!")
        tentativas -= 1  # Não conta como tentativa válida

if tentativas >= max_tentativas:
    print(f"😞 Suas tentativas acabaram! O número era {numero_secreto}")