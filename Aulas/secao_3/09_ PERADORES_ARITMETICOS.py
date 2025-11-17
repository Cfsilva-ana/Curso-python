# ============================================================
# OPERADORES ARITMÉTICOS
# ============================================================
# Operadores para cálculos matemáticos:
# + (soma), - (subtração), * (multiplicação), / (divisão)
# // (divisão inteira), % (resto), ** (potência)

print("=== Operadores Aritméticos ===")

a = 10
b = 3

print(f"{a} + {b} = {a + b}")      # 13 - Soma
print(f"{a} - {b} = {a - b}")      # 7 - Subtração
print(f"{a} * {b} = {a * b}")      # 30 - Multiplicação
print(f"{a} / {b} = {a / b:.2f}")  # 3.33 - Divisão (sempre float)
print(f"{a} // {b} = {a // b}")    # 3 - Divisão inteira (sem resto)
print(f"{a} % {b} = {a % b}")      # 1 - Resto da divisão
print(f"{a} ** {b} = {a ** b}")    # 1000 - Potência (10³)


# ============================================================
# OPERADORES DE ATRIBUIÇÃO COMPOSTOS
# ============================================================
num = 10
print(f"\nValor inicial: {num}")

num += 5    # num = num + 5
print(f"Após +=5: {num}")

num *= 2    # num = num * 2
print(f"Após *=2: {num}")

num %= 3    # num = num % 3
print(f"Após %=3: {num}")


# ============================================================
# APLICAÇÕES DO RESTO (%)
# ============================================================
print("\n=== Verificando Par/Ímpar ===")

for numero in [10, 15, 22, 33]:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")


# ============================================================
# DICAS IMPORTANTES
# ============================================================
print("\n💡 Dicas importantes:")
print("1. Divisão (/) sempre retorna float")
print("2. Divisão inteira (//) remove decimais")
print("3. Resto (%) é útil para par/ímpar")
print("4. Potência (**) pode calcular raízes")
print("5. Cuidado com divisão por zero!")
