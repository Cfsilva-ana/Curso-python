# ANALISADOR DE TEXTO
# Exemplo prático usando loops for

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

if __name__ == "__main__":
    analisar_texto("Python é incrível! 123")