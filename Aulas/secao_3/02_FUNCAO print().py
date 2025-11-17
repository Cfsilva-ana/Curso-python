# ============================================================
# 2. A FUNÇÃO print()
# ============================================================
# print() exibe informações na tela
# Aceita textos, números, variáveis e expressões

print("\n=== Exemplos de print() ===")
print("Texto simples")
print(42)
print(2 + 3)
print("A", "B", "C", sep=" - ")  # sep define o separador

# ============================================================
# PARÂMETROS AVANÇADOS DO PRINT()
# ============================================================
# \r\n -> CRLF
# \n -> LM
print("\n=== Parâmetros do print() ===")
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
