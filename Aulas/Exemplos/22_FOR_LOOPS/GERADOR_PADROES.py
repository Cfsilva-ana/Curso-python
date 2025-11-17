# GERADOR DE PADRÕES
# Exemplo prático de loops for aninhados

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
    
    print(f"Quadrado {tamanho}x{tamanho}:")
    
    for i in range(tamanho):
        if i == 0 or i == tamanho - 1:
            # Primeira e última linha - cheias
            print("*" * tamanho)
        else:
            # Linhas do meio - apenas bordas
            print("*" + " " * (tamanho - 2) + "*")

def gerar_tabuada(limite):
    """Gera tabuada usando for aninhado"""
    
    print(f"Tabuada do 1 ao {limite}:")
    for i in range(1, limite + 1):
        print(f"\nTabuada do {i}:")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j:>2} = {resultado:>3}")

if __name__ == "__main__":
    print("=== Gerador de Padrões ===")
    gerar_triangulo(5)
    print()
    gerar_quadrado(6)
    print()
    gerar_tabuada(3)