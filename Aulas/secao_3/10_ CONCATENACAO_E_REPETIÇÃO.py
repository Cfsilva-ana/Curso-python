# ============================================================
# CONCATENAÇÃO E REPETIÇÃO
# ============================================================
# + concatena strings
# * repete strings

print("=== Concatenação e Repetição ===")

# ============================================================
# 1. CONCATENAÇÃO COM +
# ============================================================
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print("Nome completo:", nome_completo)

# Concatenação múltipla
saudacao = "Olá, " + "meu " + "nome " + "é " + nome_completo + "!"
print(saudacao)


# ============================================================
# 2. REPETIÇÃO COM *
# ============================================================
print("Ha" * 5)        # HaHaHaHaHa
print("Python" * 3)    # PythonPythonPython
print("-" * 20)        # --------------------


# ============================================================
# 3. COMBINAÇÃO DE + E *
# ============================================================
# Criando padrões
print("Padrão: " + ".-" * 10)  # .-.-.-.-.-.-.-.-.-.-

# Criando bordas
largura = 25
titulo = "PYTHON"
borda = "*" * largura
print(borda)
print(titulo.center(largura))
print(borda)


# ============================================================
# 4. DICAS IMPORTANTES
# ============================================================
print("\n💡 Dicas:")
print("1. + junta strings, * repete strings")
print("2. F-strings são mais eficientes que +")
print("3. Use * para criar separadores visuais")

# Comparando métodos
nome = "Ana"
idade = 25
print(f"Concatenação: {'Olá ' + nome + ', você tem ' + str(idade) + ' anos'}")
print(f"F-string: {f'Olá {nome}, você tem {idade} anos'}")