# ============================================================
# ENTRADA DE DADOS - INPUT
# ============================================================
# input() sempre retorna STRING, mesmo com números!

print("=== Entrada de Dados ===")

# ============================================================
# 1. INPUT BÁSICO
# ============================================================
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
print(f"Tipo: {type(nome)}")  # <class 'str'>


# ============================================================
# 2. PROBLEMA: TUDO É STRING
# ============================================================
idade_str = input("Digite sua idade: ")
print(f"Idade: {idade_str} (tipo: {type(idade_str)})")

# Erro comum:
# proximo_ano = idade_str + 1  # TypeError!


# ============================================================
# 3. SOLUÇÃO: CONVERTER TIPOS
# ============================================================
idade = int(input("Digite sua idade: "))
print(f"Próximo ano: {idade + 1} anos")

altura = float(input("Digite sua altura: "))
print(f"Altura: {altura:.2f}m")


# ============================================================
# 4. TRATAMENTO DE ERROS
# ============================================================
try:
    numero = int(input("Digite um número: "))
    print(f"Dobro: {numero * 2}")
except ValueError:
    print("Erro: Digite apenas números!")


# ============================================================
# 5. VALIDAÇÃO COM LOOP
# ============================================================
while True:
    try:
        nota = float(input("Nota (0-10): "))
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        print("Nota deve estar entre 0 e 10!")
    except ValueError:
        print("Digite um número válido!")


# ============================================================
# 6. MÚLTIPLAS ENTRADAS
# ============================================================
# Método 1: split()
dados = input("Nome e idade (separados por espaço): ").split()
nome_user = dados[0]
idade_user = int(dados[1])
print(f"{nome_user} tem {idade_user} anos")

# Método 2: separado
x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))
print(f"Ponto: ({x}, {y})")

