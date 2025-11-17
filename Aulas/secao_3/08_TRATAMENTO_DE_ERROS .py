# ============================================================
# 8. TRATAMENTO DE ERROS
# ============================================================
# Nem toda conversão é possível
#
print("\n=== Tratando Erros ===")

texto_invalido = "abc123"

try:
    resultado = int(texto_invalido)
    print("Conversão bem-sucedida:", resultado)
except ValueError:
    print(f"Erro: '{texto_invalido}' não pode ser convertido para número")

print("Programa continua normalmente!")