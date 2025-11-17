# ============================================================
# FATIAMENTO DE STRINGS
# ============================================================
# Extraindo partes de strings usando índices

print("=== Fatiamento de Strings ===")

# ============================================================
# 1. ÍNDICES EM STRINGS
# ============================================================
"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [início:fim:passo]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = "Olá mundo"
print(f"String: '{variavel}'")
print(f"Tamanho: {len(variavel)} caracteres")

# Índices positivos
print("\n=== Índices Positivos ===")
print(f"Posição 0: '{variavel[0]}'")  # O
print(f"Posição 1: '{variavel[1]}'")  # l
print(f"Posição 4: '{variavel[4]}'")  # m

# Índices negativos
print("\n=== Índices Negativos ===")
print(f"Posição -1: '{variavel[-1]}'")  # o (último)
print(f"Posição -2: '{variavel[-2]}'")  # d
print(f"Posição -5: '{variavel[-5]}'")  # m


# ============================================================
# 2. FATIAMENTO BÁSICO [início:fim]
# ============================================================
print("\n=== Fatiamento Básico ===")

texto = "Python Programming"
print(f"Texto: '{texto}'")

# [início:fim] - não inclui o fim
print(f"[0:6]: '{texto[0:6]}'")    # Python
print(f"[7:18]: '{texto[7:18]}'")  # Programming
print(f"[0:3]: '{texto[0:3]}'")    # Pyt


# ============================================================
# 3. FATIAMENTO COM OMISSÕES
# ============================================================
print("\n=== Omitindo Índices ===")

# Omitir início (começa do 0)
print(f"[:6]: '{texto[:6]}'")      # Python

# Omitir fim (vai até o final)
print(f"[7:]: '{texto[7:]}'")      # Programming

# Pegar tudo
print(f"[:]: '{texto[:]}'")        # Python Programming


# ============================================================
# 4. FATIAMENTO COM PASSO [início:fim:passo]
# ============================================================
print("\n=== Fatiamento com Passo ===")

# Passo 2 (pula de 2 em 2)
print(f"[::2]: '{texto[::2]}'")    # Pto rgamn

# Passo 3
print(f"[::3]: '{texto[::3]}'")    # Ph oamn

# Passo negativo (inverte)
print(f"[::-1]: '{texto[::-1]}'")  # gnimmargorP nohtyP


# ============================================================
# 5. EXEMPLOS PRÁTICOS DE INVERSÃO
# ============================================================
print("\n=== Inversão de Strings ===")

nome = "Maria"
print(f"Nome: {nome}")
print(f"Nome invertido: {nome[::-1]}")

# Verificar se é palíndromo
palavra = "arara"
palavra_invertida = palavra[::-1]
eh_palindromo = palavra == palavra_invertida
print(f"'{palavra}' é palíndromo? {eh_palindromo}")


# ============================================================
# 6. EXTRAINDO PARTES ESPECÍFICAS
# ============================================================
print("\n=== Extraindo Partes ===")

email = "usuario@dominio.com"
print(f"Email: {email}")

# Encontrar posições importantes
arroba = email.find("@")
ponto = email.find(".")

# Extrair partes
usuario = email[:arroba]
dominio = email[arroba+1:ponto]
extensao = email[ponto+1:]

print(f"Usuário: {usuario}")
print(f"Domínio: {dominio}")
print(f"Extensão: {extensao}")


# ============================================================
# 7. FATIAMENTO COM ÍNDICES NEGATIVOS
# ============================================================
print("\n=== Índices Negativos no Fatiamento ===")

frase = "Aprendendo Python"
print(f"Frase: '{frase}'")

# Últimos 6 caracteres
print(f"Últimos 6: '{frase[-6:]}'")     # Python

# Todos menos os últimos 7
print(f"Sem últimos 7: '{frase[:-7]}'") # Aprendendo

# Do 3º ao penúltimo
print(f"[2:-1]: '{frase[2:-1]}'")       # rendendo Pytho


# ============================================================
# 8. EXEMPLO PRÁTICO: VALIDADOR DE CPF
# ============================================================
print("\n=== Validador de CPF ===")

def formatar_cpf(cpf):
    """Formata CPF removendo caracteres especiais"""
    # Remove pontos e hífens
    cpf_limpo = ""
    for char in cpf:
        if char.isdigit():
            cpf_limpo += char
    
    if len(cpf_limpo) == 11:
        # Formatar: 123.456.789-01
        parte1 = cpf_limpo[:3]
        parte2 = cpf_limpo[3:6]
        parte3 = cpf_limpo[6:9]
        parte4 = cpf_limpo[9:]
        
        cpf_formatado = f"{parte1}.{parte2}.{parte3}-{parte4}"
        return cpf_formatado
    else:
        return "CPF inválido"

# Testando
cpfs_teste = ["12345678901", "123.456.789-01", "11122233344"]
for cpf in cpfs_teste:
    resultado = formatar_cpf(cpf)
    print(f"'{cpf}' → '{resultado}'")


# ============================================================
# 9. EXEMPLO PRÁTICO: ANALISADOR DE NOME
# ============================================================
print("\n=== Analisador de Nome ===")

def analisar_nome(nome_completo):
    """Analisa um nome completo"""
    
    if not nome_completo or not nome_completo.strip():
        return "Nome vazio"
    
    nome = nome_completo.strip()
    
    print(f"Nome completo: '{nome}'")
    print(f"Nome invertido: '{nome[::-1]}'")
    
    # Verificar espaços
    if " " in nome:
        print("Contém espaços: Sim")
        partes = nome.split()
        primeiro_nome = partes[0]
        ultimo_nome = partes[-1]
        print(f"Primeiro nome: '{primeiro_nome}'")
        print(f"Último nome: '{ultimo_nome}'")
    else:
        print("Contém espaços: Não")
        primeiro_nome = nome
    
    print(f"Total de caracteres: {len(nome)}")
    print(f"Primeira letra: '{nome[0]}'")
    print(f"Última letra: '{nome[-1]}'")
    
    # Iniciais
    if " " in nome:
        iniciais = ""
        for parte in nome.split():
            if parte:  # Verifica se não está vazio
                iniciais += parte[0].upper()
        print(f"Iniciais: {iniciais}")

# Testando
print("Teste 1:")
analisar_nome("Ana Silva Santos")

print("\nTeste 2:")
analisar_nome("João")


# ============================================================
# 10. EXEMPLO PRÁTICO: EXTRATOR DE DADOS
# ============================================================
print("\n=== Extrator de Dados ===")

def extrair_dados_url(url):
    """Extrai informações de uma URL"""
    
    print(f"URL: {url}")
    
    # Remover protocolo
    if "://" in url:
        protocolo_fim = url.find("://") + 3
        protocolo = url[:protocolo_fim-3]
        resto = url[protocolo_fim:]
        print(f"Protocolo: {protocolo}")
    else:
        resto = url
        protocolo = "Não identificado"
    
    # Extrair domínio
    if "/" in resto:
        barra = resto.find("/")
        dominio = resto[:barra]
        caminho = resto[barra:]
    else:
        dominio = resto
        caminho = "/"
    
    print(f"Domínio: {dominio}")
    print(f"Caminho: {caminho}")
    
    # Extrair extensão do domínio
    if "." in dominio:
        ultimo_ponto = dominio.rfind(".")
        extensao = dominio[ultimo_ponto+1:]
        print(f"Extensão: {extensao}")

# Testando
print("Teste 1:")
extrair_dados_url("https://www.python.org/downloads/")

print("\nTeste 2:")
extrair_dados_url("github.com/usuario/projeto")


print("\n🎉 Você dominou o fatiamento de strings!")