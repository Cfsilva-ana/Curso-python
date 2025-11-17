print("\n=== Barra de Progresso ===")

def mostrar_progresso(porcentagem, largura=30):
    """Mostra uma barra de progresso"""
    
    # Calcular quantos caracteres preenchidos
    preenchidos = int(porcentagem * largura / 100)
    vazios = largura - preenchidos
    
    # Criar a barra
    barra = "[" + "█" * preenchidos + "-" * vazios + "]"
    
    # Adicionar porcentagem
    resultado = barra + f" {porcentagem:3.0f}%"
    
    return resultado

# Simulando progresso
print("Simulando download:")
for progresso in [0, 25, 50, 75, 100]:
    barra = mostrar_progresso(progresso)
    print(f"Download: {barra}")