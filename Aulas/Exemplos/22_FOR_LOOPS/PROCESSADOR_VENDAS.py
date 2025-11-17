# PROCESSADOR DE VENDAS
# Exemplo prático de processamento de dados com for

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

def analisar_estoque():
    """Analisa estoque usando for com dicionários"""
    
    estoque = {
        "Notebook": {"preco": 2500, "quantidade": 15, "minimo": 5},
        "Mouse": {"preco": 50, "quantidade": 2, "minimo": 10},
        "Teclado": {"preco": 100, "quantidade": 8, "minimo": 5},
        "Monitor": {"preco": 800, "quantidade": 3, "minimo": 2},
    }
    
    print("\nANÁLISE DE ESTOQUE")
    print("=" * 60)
    
    produtos_baixos = []
    
    for produto, dados in estoque.items():
        quantidade = dados["quantidade"]
        minimo = dados["minimo"]
        status = "⚠️ BAIXO" if quantidade <= minimo else "✅ OK"
        
        print(f"{produto:<12} | Qtd: {quantidade:>3} | Min: {minimo:>3} | {status}")
        
        if quantidade <= minimo:
            produtos_baixos.append(produto)
    
    print("=" * 60)
    if produtos_baixos:
        print("🚨 PRODUTOS COM ESTOQUE BAIXO:")
        for produto in produtos_baixos:
            print(f"  - {produto}")
    else:
        print("✅ Todos os produtos com estoque adequado!")

if __name__ == "__main__":
    processar_vendas()
    analisar_estoque()