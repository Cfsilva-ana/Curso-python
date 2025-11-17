# ============================================================
# VARIÁVEIS EM PYTHON
# ============================================================
# Variáveis são usadas para salvar algo na memória do computador
# PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _
# O sinal de = é o operador de atribuição

print("=== Variáveis em Python ===")

# ============================================================
# 1. CRIANDO VARIÁVEIS BÁSICAS
# ============================================================
# Uso: nome_variavel = expressão

print("\n=== Criando Variáveis ===")

# Variáveis básicas
nome = "Ana Silva"
idade = 25
altura = 1.65
estudante = True

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"É estudante: {estudante}")


# ============================================================
# 2. REGRAS PARA NOMES DE VARIÁVEIS
# ============================================================
print("\n=== Regras para Nomes ===")

# ✅ Nomes válidos
nome_completo = "João Silva"
idade_atual = 30
valor_1 = 100
_variavel_privada = "secreto"
PI = 3.14159  # Constante (por convenção)

# ❌ Nomes inválidos (não use):
# 1nome = "erro"      # Não pode começar com número
# nome-completo = "erro"  # Não pode ter hífen
# class = "erro"      # Não pode usar palavras reservadas

print("Exemplos de bons nomes:")
print(f"nome_completo: {nome_completo}")
print(f"idade_atual: {idade_atual}")
print(f"PI: {PI}")


# ============================================================
# 3. ATRIBUIÇÃO MÚLTIPLA
# ============================================================
print("\n=== Atribuição Múltipla ===")

# Atribuir o mesmo valor a várias variáveis
a = b = c = 10
print(f"a = {a}, b = {b}, c = {c}")

# Atribuir valores diferentes
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Trocar valores de variáveis
print(f"Antes: x = {x}, y = {y}")
x, y = y, x  # Troca os valores
print(f"Depois: x = {x}, y = {y}")


# ============================================================
# 4. VARIÁVEIS COM EXPRESSÕES
# ============================================================
print("\n=== Variáveis com Expressões ===")

# Variáveis podem armazenar resultados de expressões
num1 = 10
num2 = 5
soma = num1 + num2
multiplicacao = num1 * num2
maior_que_15 = soma > 15

print(f"num1: {num1}")
print(f"num2: {num2}")
print(f"soma: {soma}")
print(f"multiplicação: {multiplicacao}")
print(f"soma > 15: {maior_que_15}")


# ============================================================
# 5. REATRIBUIÇÃO DE VARIÁVEIS
# ============================================================
print("\n=== Reatribuição ===")

# Variáveis podem ter seus valores alterados
contador = 0
print(f"Contador inicial: {contador}")

contador = contador + 1
print(f"Após +1: {contador}")

contador += 5  # Forma abreviada
print(f"Após +5: {contador}")

contador *= 2  # Multiplica por 2
print(f"Após *2: {contador}")


# ============================================================
# 6. ESCOPO DE VARIÁVEIS (CONCEITO BÁSICO)
# ============================================================
print("\n=== Escopo Básico ===")

# Variáveis globais (disponíveis em todo o programa)
variavel_global = "Disponível em todo lugar"

def minha_funcao():
    # Variável local (só existe dentro da função)
    variavel_local = "Só existe aqui"
    print(f"Dentro da função: {variavel_global}")
    print(f"Variável local: {variavel_local}")

minha_funcao()
print(f"Fora da função: {variavel_global}")
# print(variavel_local)  # Isso daria erro!


# ============================================================
# 7. CONSTANTES (CONVENÇÃO)
# ============================================================
print("\n=== Constantes ===")

# Python não tem constantes reais, mas usa convenção
# Nomes em maiúscula indicam que não devem ser alterados
VELOCIDADE_LUZ = 299792458  # m/s
PI = 3.14159
MAX_TENTATIVAS = 3

print(f"Velocidade da luz: {VELOCIDADE_LUZ} m/s")
print(f"PI: {PI}")
print(f"Máximo de tentativas: {MAX_TENTATIVAS}")


# ============================================================
# 8. EXEMPLO PRÁTICO: CALCULADORA DE IMC
# ============================================================
print("\n=== Exemplo Prático: IMC ===")

# Dados da pessoa
nome_pessoa = "Carlos Silva"
idade_pessoa = 35
peso_kg = 80.5
altura_m = 1.78

# Cálculos
imc = peso_kg / (altura_m ** 2)
idade_em_meses = idade_pessoa * 12
maior_de_idade = idade_pessoa >= 18

# Classificação do IMC
if imc < 18.5:
    classificacao_imc = "Abaixo do peso"
elif imc < 25:
    classificacao_imc = "Peso normal"
elif imc < 30:
    classificacao_imc = "Sobrepeso"
else:
    classificacao_imc = "Obesidade"

# Resultados
print("\nFICHA PESSOAL")
print("=" * 30)
print(f"Nome: {nome_pessoa}")
print(f"Idade: {idade_pessoa} anos ({idade_em_meses} meses)")
print(f"Peso: {peso_kg} kg")
print(f"Altura: {altura_m} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")
print(f"Maior de idade: {'Sim' if maior_de_idade else 'Não'}")





# ============================================================
# 09. BOAS PRÁTICAS
# ============================================================
print("\n=== Boas Práticas ===")

print("💡 Dicas para variáveis:")
print("1. Use nomes descritivos: 'idade' em vez de 'i'")
print("2. Use snake_case: 'nome_completo'")
print("3. Constantes em MAIUSCULA: 'PI'")
print("4. Não use palavras reservadas")
print("5. Seja consistente com os nomes")

# Exemplos de bons nomes
print("\n✅ Bons exemplos:")
preco_produto = 29.99
quantidade_estoque = 150
data_nascimento = "15/03/1990"
print(f"Preço: R$ {preco_produto}")
print(f"Estoque: {quantidade_estoque} unidades")
print(f"Nascimento: {data_nascimento}")