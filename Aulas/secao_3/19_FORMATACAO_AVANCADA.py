# ============================================================
# FORMATAÇÃO AVANÇADA DE STRINGS
# ============================================================
# Técnicas avançadas para formatar texto e números

print("=== Formatação Avançada ===")

# ============================================================
# 1. INTERPOLAÇÃO COM % (MÉTODO ANTIGO)
# ============================================================
"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

print("=== Interpolação com % ===")

nome = "Luiz"
preco = 1000.95897643

# Formatação básica com %
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)

# Hexadecimal
print("O hexadecimal de %d é %08X" % (1500, 1500))

# Outros exemplos
idade = 25
print("Nome: %s, Idade: %d anos" % (nome, idade))
print("Percentual: %.1f%%" % (85.7))  # %% para mostrar %


# ============================================================
# 2. FORMATAÇÃO AVANÇADA COM F-STRINGS
# ============================================================
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

print("\n=== F-strings Avançadas ===")

variavel = "ABC"
numero = 1000.4873648123746

# Alinhamento
print(f"'{variavel}'")           # Normal
print(f"'{variavel: >10}'")      # Alinhado à direita
print(f"'{variavel: <10}.'")     # Alinhado à esquerda
print(f"'{variavel: ^10}.'")     # Centralizado

# Formatação de números
print(f"{numero:0=+10,.1f}")     # Formatação complexa
print(f"O hexadecimal de 1500 é {1500:08X}")

# Conversion flags
print(f"{variavel!r}")           # Representação
print(f"{variavel!s}")           # String
print(f"{variavel!a}")           # ASCII


# ============================================================
# 3. ALINHAMENTO E PREENCHIMENTO
# ============================================================
print("\n=== Alinhamento e Preenchimento ===")

texto = "Python"
numero = 42

# Alinhamento básico
print(f"'{texto:>15}'")    # Direita (15 caracteres)
print(f"'{texto:<15}'")    # Esquerda (15 caracteres)
print(f"'{texto:^15}'")    # Centro (15 caracteres)

# Preenchimento personalizado
print(f"'{texto:*>15}'")   # Preenche com *
print(f"'{texto:-<15}'")   # Preenche com -
print(f"'{texto:=^15}'")   # Preenche com =

# Com números
print(f"'{numero:0>5}'")   # 00042
print(f"'{numero:*^7}'")   # **42***


# ============================================================
# 4. FORMATAÇÃO DE NÚMEROS
# ============================================================
print("\n=== Formatação de Números ===")

valor = 1234567.89123
negativo = -1234.56

# Casas decimais
print(f"2 casas: {valor:.2f}")
print(f"0 casas: {valor:.0f}")
print(f"4 casas: {valor:.4f}")

# Separador de milhares
print(f"Com vírgula: {valor:,.2f}")
print(f"Com underscore: {valor:_.2f}")

# Sinal sempre visível
print(f"Positivo: {valor:+.2f}")
print(f"Negativo: {negativo:+.2f}")

# Combinando formatações
print(f"Completo: {valor:+,.2f}")
print(f"Alinhado: {valor:>15,.2f}")


# ============================================================
# 5. FORMATAÇÃO DE PORCENTAGENS
# ============================================================
print("\n=== Porcentagens ===")

decimal = 0.1234
print(f"Como decimal: {decimal}")
print(f"Como %: {decimal:.2%}")
print(f"Como % (1 casa): {decimal:.1%}")

# Exemplo prático
acertos = 85
total = 100
percentual = acertos / total
print(f"Acertos: {acertos}/{total} = {percentual:.1%}")


# ============================================================
# 6. NÚMEROS EM DIFERENTES BASES
# ============================================================
print("\n=== Diferentes Bases ===")

numero = 255

# Diferentes representações
print(f"Decimal: {numero}")
print(f"Binário: {numero:b}")
print(f"Octal: {numero:o}")
print(f"Hexadecimal: {numero:x}")
print(f"Hexadecimal maiúsculo: {numero:X}")

# Com prefixos
print(f"Binário com prefixo: {numero:#b}")
print(f"Octal com prefixo: {numero:#o}")
print(f"Hex com prefixo: {numero:#x}")

# Preenchimento com zeros
print(f"Hex 8 dígitos: {numero:08X}")
print(f"Binário 16 bits: {numero:016b}")


# ============================================================
# 7. FORMATAÇÃO DE DATA E HORA
# ============================================================
print("\n=== Data e Hora ===")

from datetime import datetime

agora = datetime.now()

# Diferentes formatos
print(f"Completo: {agora}")
print(f"Data: {agora:%d/%m/%Y}")
print(f"Hora: {agora:%H:%M:%S}")
print(f"Data e hora: {agora:%d/%m/%Y %H:%M}")
print(f"Formato US: {agora:%Y-%m-%d}")
print(f"Extenso: {agora:%A, %d de %B de %Y}")





# ============================================================
# 8. DICAS AVANÇADAS
# ============================================================
print("\n=== Dicas Avançadas ===")

print("💡 Dicas de formatação:")
print("1. F-strings são mais rápidas que % e .format()")
print("2. Use :, para separador de milhares")
print("3. Use :+ para mostrar sinal sempre")
print("4. Use :^ para centralizar")
print("5. Use :.2% para porcentagens")

# Demonstrações
valor = 1234567.89
print(f"\nExemplos:")
print(f"Valor: {valor:>15,.2f}")
print(f"Percentual: {0.1567:.1%}")
print(f"Hex: {255:08X}")
print(f"Centralizado: {'PYTHON':=^20}")


print("\n🎉 Você dominou formatação avançada!")