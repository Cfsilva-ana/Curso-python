# ============================================================
# OPERADORES EM PYTHON
# ============================================================
# Todos os operadores que você precisa conhecer

print("=== Operadores em Python ===")

# ============================================================
# 1. OPERADORES ARITMÉTICOS
# ============================================================
print("\n=== Operadores Aritméticos ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")    # Soma: 13
print(f"a - b = {a - b}")    # Subtração: 7
print(f"a * b = {a * b}")    # Multiplicação: 30
print(f"a / b = {a / b}")    # Divisão: 3.333...
print(f"a // b = {a // b}")  # Divisão inteira: 3
print(f"a % b = {a % b}")    # Resto: 1
print(f"a ** b = {a ** b}")  # Potência: 1000


# ============================================================
# 2. OPERADORES DE COMPARAÇÃO
# ============================================================
print("\n=== Operadores de Comparação ===")

x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")   # Igual: False
print(f"x != y: {x != y}")   # Diferente: True
print(f"x > y: {x > y}")     # Maior: False
print(f"x < y: {x < y}")     # Menor: True
print(f"x >= y: {x >= y}")   # Maior ou igual: False
print(f"x <= y: {x <= y}")   # Menor ou igual: True


# ============================================================
# 3. OPERADORES LÓGICOS
# ============================================================
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

print("\n=== Operadores Lógicos ===")

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # E: False
print(f"p or q: {p or q}")    # OU: True
print(f"not p: {not p}")      # NÃO: False
print(f"not q: {not q}")      # NÃO: True

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)

# Exemplos práticos
idade = 20
tem_carteira = True

print(f"\nIdade: {idade}, Tem carteira: {tem_carteira}")
print(f"Pode dirigir: {idade >= 18 and tem_carteira}")


# ============================================================
# 4. OPERADORES DE ATRIBUIÇÃO
# ============================================================
print("\n=== Operadores de Atribuição ===")

num = 10
print(f"Inicial: {num}")

num += 5    # num = num + 5
print(f"Após +=5: {num}")

num -= 3    # num = num - 3
print(f"Após -=3: {num}")

num *= 2    # num = num * 2
print(f"Após *=2: {num}")

num /= 4    # num = num / 4
print(f"Após /=4: {num}")

num //= 2   # num = num // 2
print(f"Após //=2: {num}")

num %= 3    # num = num % 3
print(f"Após %=3: {num}")

num **= 3   # num = num ** 3
print(f"Após **=3: {num}")


# ============================================================
# 5. OPERADORES DE IDENTIDADE
# ============================================================
print("\n=== Operadores de Identidade ===")

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1: {lista1}")
print(f"lista2: {lista2}")
print(f"lista3: {lista3}")

print(f"lista1 == lista2: {lista1 == lista2}")  # Mesmo conteúdo: True
print(f"lista1 is lista2: {lista1 is lista2}")  # Mesmo objeto: False
print(f"lista1 is lista3: {lista1 is lista3}")  # Mesmo objeto: True

# Com números pequenos (cache do Python)
a = 5
b = 5
print(f"a is b (números pequenos): {a is b}")  # True (cache)

# is not
print(f"lista1 is not lista2: {lista1 is not lista2}")  # True


# ============================================================
# 6. OPERADORES DE ASSOCIAÇÃO (IN / NOT IN)
# ============================================================
# Verificação de conteúdo em sequências

print("\n=== Operadores de Associação ===")

nome = 'Luiz'
print(f"Nome: {nome}")
print(f"nome[2]: {nome[2]}")
print(f"nome[-4]: {nome[-4]}")
print(f"'uiz' in nome: {'uiz' in nome}")
print(f"'zip' in nome: {'zip' in nome}")
print(f"nome[0:2]: {nome[0:2]}")
print(f"nome[:2]: {nome[:2]}")
print(f"nome[2:]: {nome[2:]}")
print(f"nome[:]: {nome[:]}")
print(f"nome[-4:-1]: {nome[-4:-1]}")

texto = "Python"
lista = [1, 2, 3, 4, 5]
dicionario = {"nome": "Ana", "idade": 25}

print(f"\nTexto: '{texto}'")
print(f"'P' in texto: {'P' in texto}")        # True
print(f"'x' in texto: {'x' in texto}")        # False
print(f"'z' not in texto: {'z' not in texto}")  # True

print(f"\nLista: {lista}")
print(f"3 in lista: {3 in lista}")            # True
print(f"6 in lista: {6 in lista}")            # False

print(f"\nDicionário: {dicionario}")
print(f"'nome' in dicionario: {'nome' in dicionario}")      # True
print(f"'Ana' in dicionario: {'Ana' in dicionario}")        # False (busca chaves)


# ============================================================
# 7. PRECEDÊNCIA DOS OPERADORES
# ============================================================
print("\n=== Precedência dos Operadores ===")

# Ordem de precedência (maior para menor):
# 1. ** (potência)
# 2. *, /, //, % (multiplicação, divisão)
# 3. +, - (soma, subtração)
# 4. ==, !=, <, >, <=, >= (comparação)
# 5. not (negação lógica)
# 6. and (E lógico)
# 7. or (OU lógico)

resultado1 = 2 + 3 * 4
resultado2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {resultado1}")      # 14
print(f"(2 + 3) * 4 = {resultado2}")    # 20

resultado3 = 2 ** 3 * 4
resultado4 = 2 ** (3 * 4)
print(f"2 ** 3 * 4 = {resultado3}")     # 32
print(f"2 ** (3 * 4) = {resultado4}")   # 4096

# Lógicos
resultado5 = True or False and False
resultado6 = (True or False) and False
print(f"True or False and False = {resultado5}")      # True
print(f"(True or False) and False = {resultado6}")    # False


# ============================================================
# 8. OPERADORES BIT A BIT (BITWISE)
# ============================================================
print("\n=== Operadores Bit a Bit ===")

a = 5   # 101 em binário
b = 3   # 011 em binário

print(f"a = {a} ({bin(a)}), b = {b} ({bin(b)})")
print(f"a & b = {a & b} ({bin(a & b)})")    # AND: 001 = 1
print(f"a | b = {a | b} ({bin(a | b)})")    # OR: 111 = 7
print(f"a ^ b = {a ^ b} ({bin(a ^ b)})")    # XOR: 110 = 6
print(f"~a = {~a} ({bin(~a)})")             # NOT: complemento
print(f"a << 1 = {a << 1} ({bin(a << 1)})")  # Shift esquerda: 1010 = 10
print(f"a >> 1 = {a >> 1} ({bin(a >> 1)})")  # Shift direita: 10 = 2


# ============================================================
# 9. OPERADOR TERNÁRIO (CONDICIONAL)
# ============================================================
print("\n=== Operador Ternário ===")

idade = 20
status = "maior" if idade >= 18 else "menor"
print(f"Idade: {idade} - Status: {status}")

# Equivale a:
# if idade >= 18:
#     status = "maior"
# else:
#     status = "menor"

# Mais exemplos
numero = -5
resultado = "positivo" if numero > 0 else "negativo ou zero"
print(f"Número {numero} é {resultado}")

nota = 8.5
situacao = "aprovado" if nota >= 7 else "reprovado"
print(f"Nota {nota}: {situacao}")





print("\n🎉 Você dominou todos os operadores!")