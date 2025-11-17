# ============================================================
# CONDICIONAIS - IF / ELIF / ELSE
# ============================================================
# Tomando decisões no código

print("=== Estruturas Condicionais ===")

# ============================================================
# 1. BLOCOS DE CÓDIGO E INDENTAÇÃO
# ============================================================
# Python usa INDENTAÇÃO (espaços) para definir blocos
# Use 4 espaços ou 1 tab (seja consistente!)

idade = 18

if idade >= 18:
    print("Você é maior de idade")  # 4 espaços de indentação
    print("Pode votar!")            # mesmo nível
print("Esta linha sempre executa")  # fora do bloco


# ============================================================
# 2. IF SIMPLES
# ============================================================
# if condição:
#     código se verdadeiro

numero = 10

if numero > 0:
    print("Número é positivo")

if numero % 2 == 0:
    print("Número é par")


# ============================================================
# 3. IF / ELSE
# ============================================================
# if condição:
#     código se verdadeiro
# else:
#     código se falso

idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# ============================================================
# 4. OPERADORES DE COMPARAÇÃO
# ============================================================
# ==  igual
# !=  diferente
# >   maior
# <   menor
# >=  maior ou igual
# <=  menor ou igual

a = 10
b = 20

print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} > {b}: {a > b}")    # False
print(f"{a} < {b}: {a < b}")    # True


# ============================================================
# 5. FLUXO DO INTERPRETADOR EM CONDICIONAIS
# ============================================================
# O Python testa as condições EM ORDEM e para na primeira TRUE

print("\n=== Entendendo o Fluxo ===")

# Exemplo 1: Fluxo normal
nota = 8.5
print(f"Testando nota {nota}:")

if nota >= 9:
    print("1. Testou >= 9: False, continua...")
    print("Excelente!")
elif nota >= 7:
    print("2. Testou >= 7: True, PARA AQUI!")
    print("Bom!")
elif nota >= 5:
    print("3. Esta condição NÃO será testada")
    print("Regular")
else:
    print("4. Este bloco NÃO será executado")
    print("Insuficiente")

print("Fim do bloco condicional\n")


# ============================================================
# 6. DEMONSTRAÇÃO PASSO A PASSO
# ============================================================
# Vamos "simular" o interpretador

print("=== Simulando o Interpretador ===")

valor = 15
print(f"Valor a testar: {valor}")
print("Iniciando testes...")

if valor > 20:
    print(" Condição 1 (> 20): VERDADEIRA")
    print("Resultado: Valor alto")
    print(" PARA AQUI - não testa mais nada")
elif valor > 10:
    print(" Condição 2 (> 10): VERDADEIRA")
    print("Resultado: Valor médio")
    print(" PARA AQUI - não testa mais nada")
elif valor > 5:
    print(" Esta condição não será testada")
    print("Resultado: Valor baixo")
else:
    print(" Este bloco não será executado")
    print("Resultado: Valor muito baixo")

print("Fim da execução\n")


# ============================================================
# 7. PROBLEMA COMUM: ORDEM INCORRETA
# ============================================================
# ERRO: Colocar condições mais específicas depois das gerais

print("=== Erro Comum: Ordem Incorreta ===")

idade = 17
print(f"Idade: {idade}")

# ❌ ORDEM ERRADA
if idade >= 0:
    print("Pessoa existe (sempre será True para idades válidas)")
    print(" Para aqui - nunca testa as outras condições!")
elif idade >= 18:
    print(" NUNCA executará - condição inalcançável")
    print("Maior de idade")
elif idade >= 65:
    print(" NUNCA executará - condição inalcançável")
    print("Idoso")
else:
    print(" NUNCA executará")

print("\n ORDEM CORRETA seria:")
print("if idade >= 65: idoso")
print("elif idade >= 18: adulto")
print("elif idade >= 0: criança/adolescente")
print("else: idade inválida\n")


# ============================================================
# 8. COMPARAÇÃO: IF vs IF/ELIF
# ============================================================
# Diferença entre múltiplos IF e IF/ELIF

print("=== IF vs IF/ELIF ===")

numero = 15
print(f"Número: {numero}")

print("\n Múltiplos IF (testa TODOS):")
if numero > 10:
    print("Maior que 10")
if numero > 5:
    print("Maior que 5")
if numero > 0:
    print("Maior que 0")

print("\n IF/ELIF (para no primeiro True):")
if numero > 10:
    print("Maior que 10 - PARA AQUI")
elif numero > 5:
    print(" Não executa")
elif numero > 0:
    print(" Não executa")

