# ANALISADOR DE TEXTO
# Exemplo prático de fatiamento de strings

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
        
        # Iniciais
        iniciais = ""
        for parte in nome.split():
            if parte:
                iniciais += parte[0].upper()
        print(f"Iniciais: {iniciais}")
    else:
        print("Contém espaços: Não")
    
    print(f"Total de caracteres: {len(nome)}")
    print(f"Primeira letra: '{nome[0]}'")
    print(f"Última letra: '{nome[-1]}'")

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

if __name__ == "__main__":
    print("=== Formatador de CPF ===")
    cpfs_teste = ["12345678901", "123.456.789-01", "11122233344"]
    for cpf in cpfs_teste:
        resultado = formatar_cpf(cpf)
        print(f"'{cpf}' → '{resultado}'")
    
    print("\n=== Analisador de Nome ===")
    analisar_nome("Ana Silva Santos")
    
    print("\n=== Extrator de URL ===")
    extrair_dados_url("https://www.python.org/downloads/")