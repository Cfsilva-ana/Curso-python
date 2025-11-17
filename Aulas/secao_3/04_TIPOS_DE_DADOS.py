# ============================================================
# TIPOS DE DADOS EM PYTHON
# ============================================================
# Python tem 4 tipos primitivos básicos

print("=== Tipos de Dados ===")

# ============================================================
# 1. TIPO STR (STRING) - TEXTO
# ============================================================
# Strings são textos entre aspas
"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

nome = "Ana Silva"
frase = 'Python é incrível!'
texto_longo = """Este é um texto
que ocupa várias linhas"""

print("\n=== Tipo str (String) ===")
print(f"Nome: {nome} | Tipo: {type(nome)}")
print(f"Frase: {frase} | Tipo: {type(frase)}")
print(f"Tamanho do nome: {len(nome)} caracteres")

# Métodos úteis de string
print(f"Nome em maiúscula: {nome.upper()}")
print(f"Nome em minúscula: {nome.lower()}")
print(f"Primeira letra: {nome[0]}")

# Diferentes tipos de aspas
print("\n=== Strings e Aspas ===")
print(1234)

# Aspas simples
print('Min Edw')
print(1, 'Min "Edw"')

# Aspas duplas
print("Min Edw")
print(2, "Min 'Edw'")

# Escape
print("Min \"Edw\"")

# r (raw string)
print(r"Min \"Edw\"")


# ============================================================
# 2. TIPO INT (INTEGER) - NÚMEROS INTEIROS
# ============================================================
# Números sem casas decimais

idade = 25
ano_nascimento = 1998
temperatura = -5

print("\n=== Tipo int (Integer) ===")
print(f"Idade: {idade} | Tipo: {type(idade)}")
print(f"Ano: {ano_nascimento} | Tipo: {type(ano_nascimento)}")
print(f"Temperatura: {temperatura} | Tipo: {type(temperatura)}")

# Operações com int
print(f"Idade + 10: {idade + 10}")
print(f"Idade é par? {idade % 2 == 0}")


# ============================================================
# 3. TIPO FLOAT - NÚMEROS DECIMAIS
# ============================================================
# Números com ponto flutuante

altura = 1.75
peso = 70.5
preco = 29.99

print("\n=== Tipo float ===")
print(f"Altura: {altura} | Tipo: {type(altura)}")
print(f"Peso: {peso} | Tipo: {type(peso)}")
print(f"Preço: {preco} | Tipo: {type(preco)}")

# Cálculos com float
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")


# ============================================================
# 4. TIPO BOOL (BOOLEAN) - VERDADEIRO/FALSO
# ============================================================
# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro

estudante = True
maior_de_idade = idade >= 18
tem_desconto = False

print("\n=== Tipo bool (Boolean) ===")
print(f"É estudante: {estudante} | Tipo: {type(estudante)}")
print(f"É maior de idade: {maior_de_idade} | Tipo: {type(maior_de_idade)}")
print(f"Tem desconto: {tem_desconto} | Tipo: {type(tem_desconto)}")

# Exemplos básicos de bool
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# Operações lógicas
print(f"Estudante E maior de idade: {estudante and maior_de_idade}")
print(f"Estudante OU tem desconto: {estudante or tem_desconto}")


# ============================================================
# 5. VERIFICANDO TIPOS COM TYPE()
# ============================================================
print("\n=== Verificando Todos os Tipos ===")

variáveis = {
    "nome": nome,
    "idade": idade, 
    "altura": altura,
    "estudante": estudante,
    "imc": imc
}

for variavel, valor in variáveis.items():
    tipo = type(valor).__name__
    print(f"{variavel}: {valor} ({tipo})")


# ============================================================
# 6. CONVERSÃO ENTRE TIPOS
# ============================================================
print("\n=== Conversão de Tipos ===")

# String para número
idade_str = "30"
idade_int = int(idade_str)
print(f"'{idade_str}' (str) → {idade_int} (int)")

# Número para string
idade_volta = str(idade_int)
print(f"{idade_int} (int) → '{idade_volta}' (str)")

# Float para int (perde decimais)
altura_int = int(altura)
print(f"{altura} (float) → {altura_int} (int)")

# Qualquer coisa para bool
print(f"bool(0): {bool(0)}")      # False
print(f"bool(1): {bool(1)}")      # True
print(f"bool(''): {bool('')}")    # False
print(f"bool('texto'): {bool('texto')}")  # True


