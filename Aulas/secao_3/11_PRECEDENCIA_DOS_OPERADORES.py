# ============================================================
# 11. PRECEDÊNCIA DOS OPERADORES
# ============================================================
# Ordem de execução (do maior para menor):
# 1. ** (potência)
# 2. *, /, //, % (multiplicação, divisão)
# 3. +, - (soma, subtração)
# Use parênteses para alterar a ordem

print("\n=== Precedência dos Operadores ===")
resultado1 = 2 + 3 * 4
resultado2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {resultado1}")      # 14
print(f"(2 + 3) * 4 = {resultado2}")    # 20

resultado3 = 2 ** 3 * 4
resultado4 = 2 ** (3 * 4)
print(f"2 ** 3 * 4 = {resultado3}")     # 32
print(f"2 ** (3 * 4) = {resultado4}")   # 4096