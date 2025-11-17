# TIPOS NUMÉRICOS - Int e Float Detalhados
# Explorando números inteiros e decimais em profundidade

# 1. NÚMEROS INTEIROS (int)
inteiro_positivo = 42
inteiro_negativo = -17
inteiro_zero = 0

# Diferentes bases numéricas
binario = 0b1010  # Base 2 (decimal: 10)
octal = 0o12      # Base 8 (decimal: 10)  
hexadecimal = 0xA # Base 16 (decimal: 10)

print(f"Binário 0b1010 = {binario}")
print(f"Octal 0o12 = {octal}")
print(f"Hexadecimal 0xA = {hexadecimal}")

# 2. NÚMEROS DECIMAIS (float)
decimal_simples = 3.14
decimal_negativo = -2.5
notacao_cientifica = 1.5e3  # 1.5 × 10³ = 1500
notacao_pequena = 2.5e-2    # 2.5 × 10⁻² = 0.025

print(f"Notação científica 1.5e3 = {notacao_cientifica}")
print(f"Notação pequena 2.5e-2 = {notacao_pequena}")

# 3. OPERAÇÕES ESPECIAIS
divisao_inteira = 17 // 5    # Resultado: 3
resto_divisao = 17 % 5       # Resultado: 2
potenciacao = 2 ** 8         # Resultado: 256

# 4. FUNÇÕES ÚTEIS
numero = 3.7
print(f"Valor absoluto de -5: {abs(-5)}")
print(f"Arredondamento de {numero}: {round(numero)}")
print(f"Parte inteira: {int(numero)}")
print(f"Máximo entre 10 e 20: {max(10, 20)}")
print(f"Mínimo entre 10 e 20: {min(10, 20)}")

# 5. VERIFICAÇÃO DE TIPOS
print(f"Tipo de 42: {type(42)}")
print(f"Tipo de 3.14: {type(3.14)}")
print(f"É inteiro? {isinstance(42, int)}")
print(f"É float? {isinstance(3.14, float)}")

print("\nDominando tipos numéricos em Python!")