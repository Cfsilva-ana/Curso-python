# ============================================================
# 12. F-STRINGS (FORMATAÇÃO MODERNA) - RECOMENDADO!
# ============================================================
# f"texto {variável}" - forma moderna de formatar strings
# Mais legível, rápida e fácil de usar

print("\n=== F-strings ===")
nome = "Maria"
idade = 30
salario = 2500.75

# Formatação básica
print(f"Olá, eu sou {nome} e tenho {idade} anos")

# Formatação com cálculos diretos
print(f"Daqui a 5 anos terei {idade + 5} anos")
print(f"Meu nome tem {len(nome)} letras")

# Formatação de números
print(f"Salário: R$ {salario:.2f}")     # 2 casas decimais
print(f"Salário: R$ {salario:,.2f}")    # Com separador de milhares
print(f"Porcentagem: {0.85:.1%}")       # Como porcentagem