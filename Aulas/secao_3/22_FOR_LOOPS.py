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
# 7. EXEMPLO PRÁTICO: ANÁLISE DE TEXTO
# ============================================================
print("\n=== Análise de Texto ===")

def analisar_texto(texto):
    """Analisa características de um texto"""
    
    print(f"Analisando: '{texto}'")
    
    # Contadores
    vogais = 0
    consoantes = 0
    espacos = 0
    numeros = 0
    especiais = 0
    
    # Percorrer cada caractere
    for char in texto:
        if char.lower() in 'aeiou':
            vogais += 1
        elif char.isalpha():
            consoantes += 1
        elif char.isspace():
            espacos += 1
        elif char.isdigit():
            numeros += 1
        else:
            especiais += 1
    
    # Resultados
    print(f"Vogais: {vogais}")
    print(f"Consoantes: {consoantes}")
    print(f"Espaços: {espacos}")
    print(f"Números: {numeros}")
    print(f"Caracteres especiais: {especiais}")
    print(f"Total: {len(texto)} caracteres")

# Testando
analisar_texto("Python é incrível! 123")


# ============================================================
# 8. EXEMPLO PRÁTICO: GERADOR DE PADRÕES
# ============================================================
print("\n=== Gerador de Padrões ===")

def gerar_triangulo(altura):
    """Gera um triângulo de asteriscos"""
    
    print(f"Triângulo com altura {altura}:")
    
    for i in range(1, altura + 1):
        # Espaços para centralizar
        espacos = " " * (altura - i)
        # Asteriscos
        asteriscos = "*" * (2 * i - 1)
        print(espacos + asteriscos)

def gerar_quadrado(tamanho):
    """Gera um quadrado de asteriscos"""
    
    print(f"\nQuadrado {tamanho}x{tamanho}:")
    
    for i in range(tamanho):
        if i == 0 or i == tamanho - 1:
            # Primeira e última linha - cheias
            print("*" * tamanho)
        else:
            # Linhas do meio - apenas bordas
            print("*" + " " * (tamanho - 2) + "*")

# Testando
gerar_triangulo(5)
gerar_quadrado(6)


# ============================================================
# 9. EXEMPLO PRÁTICO: PROCESSADOR DE DADOS
# ============================================================
print("\n=== Processador de Dados ===")

def processar_vendas():
    """Processa dados de vendas"""
    
    vendas = [
        {"produto": "Notebook", "preco": 2500, "quantidade": 3},
        {"produto": "Mouse", "preco": 50, "quantidade": 10},
        {"produto": "Teclado", "preco": 100, "quantidade": 5},
        {"produto": "Monitor", "preco": 800, "quantidade": 2},
    ]
    
    print("RELATÓRIO DE VENDAS")
    print("=" * 50)
    
    total_geral = 0
    
    for venda in vendas:
        produto = venda["produto"]
        preco = venda["preco"]
        quantidade = venda["quantidade"]
        subtotal = preco * quantidade
        total_geral += subtotal
        
        print(f"{produto:<12} | R$ {preco:>6.2f} | {quantidade:>3} un | R$ {subtotal:>8.2f}")
    
    print("=" * 50)
    print(f"{'TOTAL GERAL':<12} | {'':<10} | {'':<6} | R$ {total_geral:>8.2f}")

processar_vendas()


# ============================================================
# 10. EXEMPLO PRÁTICO: VALIDADOR DE SENHA
# ============================================================
print("\n=== Validador de Senha ===")

def validar_senha_completa(senha):
    """Valida uma senha com múltiplos critérios"""
    
    print(f"Validando senha: {'*' * len(senha)}")
    
    # Critérios
    criterios = {
        "tamanho": len(senha) >= 8,
        "maiuscula": False,
        "minuscula": False,
        "numero": False,
        "especial": False
    }
    
    especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Verificar cada caractere
    for char in senha:
        if char.isupper():
            criterios["maiuscula"] = True
        elif char.islower():
            criterios["minuscula"] = True
        elif char.isdigit():
            criterios["numero"] = True
        elif char in especiais:
            criterios["especial"] = True
    
    # Mostrar resultados
    print("Critérios:")
    for criterio, atendido in criterios.items():
        status = "✅" if atendido else "❌"
        print(f"{status} {criterio.replace('_', ' ').title()}")
    
    # Força da senha
    pontos = sum(criterios.values())
    
    if pontos == 5:
        forca = "Muito forte"
    elif pontos >= 4:
        forca = "Forte"
    elif pontos >= 3:
        forca = "Média"
    else:
        forca = "Fraca"
    
    print(f"\nForça da senha: {forca} ({pontos}/5)")
    
    return pontos >= 4

# Testando
senhas_teste = ["123456", "MinhaSenh@123", "password", "S3nh@F0rt3!"]

for senha in senhas_teste:
    print(f"\nTeste: {senha}")
    validar_senha_completa(senha)


# ============================================================
# 11. COMPREENSÃO DE LISTAS (LIST COMPREHENSION)
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
# 12. DICAS IMPORTANTES
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