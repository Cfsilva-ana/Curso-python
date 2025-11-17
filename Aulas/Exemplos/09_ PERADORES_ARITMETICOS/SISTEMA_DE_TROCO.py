print("\n=== Sistema de Troco ===")

def calcular_troco(valor_pago, valor_produto):
    """Calcula o troco em notas e moedas"""
    
    troco = valor_pago - valor_produto
    
    if troco < 0:
        return "Valor insuficiente!"
    
    print(f"Troco: R$ {troco:.2f}")
    
    # Notas e moedas disponíveis (em centavos para evitar float)
    troco_centavos = int(troco * 100)
    
    notas_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    nomes = ["R$ 100", "R$ 50", "R$ 20", "R$ 10", "R$ 5", "R$ 2", "R$ 1", 
             "50 centavos", "25 centavos", "10 centavos", "5 centavos", "1 centavo"]
    
    print("Troco detalhado:")
    for i, valor in enumerate(notas_moedas):
        quantidade = troco_centavos // valor
        if quantidade > 0:
            print(f"{quantidade} x {nomes[i]}")
            troco_centavos %= valor

# Testando o sistema de troco
calcular_troco(50.00, 23.75)