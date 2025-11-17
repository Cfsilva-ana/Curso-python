# GERADOR DE RELATÓRIO
# Exemplo prático de formatação avançada

def gerar_relatorio_vendas():
    """Gera um relatório bem formatado"""
    
    produtos = [
        {"nome": "Notebook", "preco": 2500.99, "estoque": 15},
        {"nome": "Mouse", "preco": 45.50, "estoque": 120},
        {"nome": "Teclado", "preco": 89.90, "estoque": 75},
        {"nome": "Monitor", "preco": 899.00, "estoque": 8},
    ]
    
    print("=" * 60)
    print("RELATÓRIO DE ESTOQUE".center(60))
    print("=" * 60)
    
    # Cabeçalho
    print(f"{'Produto':<15} {'Preço':>10} {'Estoque':>8} {'Total':>12}")
    print("-" * 60)
    
    total_geral = 0
    
    for produto in produtos:
        nome = produto["nome"]
        preco = produto["preco"]
        estoque = produto["estoque"]
        total = preco * estoque
        total_geral += total
        
        print(f"{nome:<15} {preco:>10.2f} {estoque:>8} {total:>12.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL GERAL':>35} {total_geral:>12.2f}")
    print("=" * 60)

def tabela_precos():
    """Cria uma tabela de preços formatada"""
    
    precos = {
        "Básico": 29.90,
        "Intermediário": 59.90,
        "Avançado": 99.90,
        "Premium": 149.90
    }
    
    print("┌" + "─" * 25 + "┐")
    print("│" + "TABELA DE PREÇOS".center(25) + "│")
    print("├" + "─" * 25 + "┤")
    
    for plano, preco in precos.items():
        desconto = preco * 0.1  # 10% de desconto
        preco_final = preco - desconto
        
        print(f"│ {plano:<12} │")
        print(f"│ De: R$ {preco:>6.2f}    │")
        print(f"│ Por: R$ {preco_final:>5.2f}   │")
        print(f"│ Economia: {(desconto/preco)*100:>3.0f}%   │")
        
        if plano != "Premium":
            print("├" + "─" * 25 + "┤")
    
    print("└" + "─" * 25 + "┘")

if __name__ == "__main__":
    print("=== Gerador de Relatório ===")
    gerar_relatorio_vendas()
    
    print("\n=== Tabela de Preços ===")
    tabela_precos()