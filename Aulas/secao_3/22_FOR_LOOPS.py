# ============================================================
# LOOPS FOR - ITERAÇÕES
# ============================================================
# Percorrendo sequências de forma elegante

print("=== Loops For ===")

# ============================================================
# 1. CONCEITO BÁSICO DO FOR
# ============================================================
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

print("=== For Básico ===")

# For com string
texto = "Python"
print(f"Percorrendo '{texto}':")

for letra in texto:
    print(f"Letra: {letra}")


# ============================================================
# 2. FOR COM RANGE()
# ============================================================
print("\n=== For com range() ===")

# range(fim) - de 0 até fim-1
print("range(5):")
for i in range(5):
    print(f"i = {i}")

# range(início, fim) - de início até fim-1
print("\nrange(2, 7):")
for i in range(2, 7):
    print(f"i = {i}")

# range(início, fim, passo)
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"i = {i}")


# ============================================================
# 3. FOR COM LISTAS
# ============================================================
print("\n=== For com Listas ===")

frutas = ["maçã", "banana", "laranja", "uva"]
print("Frutas disponíveis:")

for fruta in frutas:
    print(f" {fruta}")

# For com índices usando enumerate()
print("\nCom índices:")
for indice, fruta in enumerate(frutas):
    print(f"{indice + 1}. {fruta}")


# ============================================================
# 4. FOR COM DICIONÁRIOS
# ============================================================
print("\n=== For com Dicionários ===")

pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo",
    "profissao": "Desenvolvedora"
}

# Percorrer chaves
print("Chaves:")
for chave in pessoa:
    print(f"Chave: {chave}")

# Percorrer valores
print("\nValores:")
for valor in pessoa.values():
    print(f"Valor: {valor}")

# Percorrer chaves e valores
print("\nChaves e valores:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# ============================================================
# 5. BREAK E CONTINUE NO FOR
# ============================================================
print("\n=== Break e Continue ===")

# Break - sai do loop
print("Procurando a letra 'o':")
for letra in "Python":
    if letra == 'o':
        print(f"Encontrei '{letra}'! Parando...")
        break
    print(f"Letra: {letra}")

# Continue - pula para próxima iteração
print("\nPulando vogais:")
for letra in "Python":
    if letra.lower() in 'aeiou':
        continue  # Pula vogais
    print(f"Consoante: {letra}")


# ============================================================
# 6. FOR ANINHADO (NESTED)
# ============================================================
print("\n=== For Aninhado ===")

# Tabuada
print("Tabuada do 1 ao 3:")
for i in range(1, 4):
    print(f"\nTabuada do {i}:")
    for j in range(1, 6):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")





# ============================================================
# 7. COMPREENSÃO DE LISTAS (LIST COMPREHENSION)
# ============================================================
print("\n=== List Comprehension ===")

# Forma tradicional
quadrados_tradicional = []
for i in range(1, 6):
    quadrados_tradicional.append(i ** 2)

# List comprehension
quadrados_comprehension = [i ** 2 for i in range(1, 6)]

print("Quadrados (tradicional):", quadrados_tradicional)
print("Quadrados (comprehension):", quadrados_comprehension)

# Com condição
pares = [i for i in range(1, 11) if i % 2 == 0]
print("Números pares:", pares)


# ============================================================
# 8. DICAS IMPORTANTES
# ============================================================
print("\n=== Dicas Importantes ===")

print("💡 Dicas sobre for:")
print("1. Use for para percorrer sequências")
print("2. range() é útil para números sequenciais")
print("3. enumerate() dá índice + valor")
print("4. items() percorre chave + valor em dicts")
print("5. List comprehension é mais eficiente")
print("6. break sai do loop, continue pula iteração")

# Demonstração
print("\nExemplo eficiente:")
numeros = [1, 2, 3, 4, 5]
dobrados = [n * 2 for n in numeros]
print(f"Originais: {numeros}")
print(f"Dobrados: {dobrados}")


print("\n🎉 Você dominou loops for!")