
print("\n=== ASCII Art ===")

def criar_caixa_texto(texto, caractere="*"):
    """Cria uma caixa ao redor do texto"""
    
    largura = len(texto) + 4
    
    # Linha superior
    caixa = caractere * largura + "\n"
    
    # Linha do meio com texto
    caixa += caractere + " " + texto + " " + caractere + "\n"
    
    # Linha inferior
    caixa += caractere * largura
    
    return caixa

# Testando diferentes estilos
textos = ["PYTHON", "PROGRAMAÇÃO", "SUCESSO"]
caracteres = ["*", "#", "="]

for i, texto in enumerate(textos):
    caixa = criar_caixa_texto(texto, caracteres[i])
    print(caixa + "\n")
