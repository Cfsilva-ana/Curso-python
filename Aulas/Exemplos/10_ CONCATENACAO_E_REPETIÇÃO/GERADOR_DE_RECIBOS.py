print("\n=== Gerador de Recibos ===")

def gerar_recibo(cliente, itens_compra):
    """Gera um recibo formatado"""
    
    # Cabeçalho
    nome_loja = "SUPERMERCADO PYTHON"
    largura = 40
    
    recibo = "\n" + "=" * largura + "\n"
    recibo += nome_loja.center(largura) + "\n"
    recibo += "=" * largura + "\n"
    recibo += f"Cliente: {cliente}" + "\n"
    recibo += "-" * largura + "\n"
    
    # Itens
    total = 0
    for item, preco in itens_compra:
        linha = item + " " + "." * (25 - len(item)) + f" R$ {preco:6.2f}\n"
        recibo += linha
        total += preco
    
    # Rodapé
    recibo += "-" * largura + "\n"
    recibo += "TOTAL" + " " + "." * 20 + f" R$ {total:6.2f}\n"
    recibo += "=" * largura + "\n"
    recibo += "Obrigado pela preferência!".center(largura) + "\n"
    recibo += "=" * largura
    
    return recibo

# Testando o gerador
compras = [
    ("Arroz 5kg", 12.50),
    ("Feijão 1kg", 8.90),
    ("Açúcar 1kg", 4.20),
    ("Leite 1L", 3.80)
]

recibo_final = gerar_recibo("Maria Silva", compras)
print(recibo_final)
