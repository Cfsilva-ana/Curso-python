# ============================================================
# 6. CONVERSÃO DE TIPOS
# ============================================================
# Transformar um tipo em outro usando:
# int(), float(), str(), bool()

print("\n=== Convertendo Tipos ===")

# Número para texto
numero = 42
numero_texto = str(numero)
print(f"'{numero_texto}' é do tipo:", type(numero_texto))

# Texto para número
texto = "100"
texto_numero = int(texto)
print(f"{texto_numero} é do tipo:", type(texto_numero))

# Inteiro para decimal
inteiro = 5
decimal = float(inteiro)
print(f"{decimal} é do tipo:", type(decimal))