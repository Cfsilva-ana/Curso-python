# VALIDADOR DE SENHA
# Exemplo prático de validação usando for

def validar_senha_completa(senha):
    """Valida uma senha com múltiplos critérios"""
    
    print(f"Validando senha: {'*' * len(senha)}")
    
    # Critérios
    criterios = {
        "tamanho": len(senha) >= 8,
        "maiuscula": False,
        "minuscula": False,
        "numero": False,
        "especial": False
    }
    
    especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Verificar cada caractere
    for char in senha:
        if char.isupper():
            criterios["maiuscula"] = True
        elif char.islower():
            criterios["minuscula"] = True
        elif char.isdigit():
            criterios["numero"] = True
        elif char in especiais:
            criterios["especial"] = True
    
    # Mostrar resultados
    print("Critérios:")
    for criterio, atendido in criterios.items():
        status = "✅" if atendido else "❌"
        print(f"{status} {criterio.replace('_', ' ').title()}")
    
    # Força da senha
    pontos = sum(criterios.values())
    
    if pontos == 5:
        forca = "Muito forte"
    elif pontos >= 4:
        forca = "Forte"
    elif pontos >= 3:
        forca = "Média"
    else:
        forca = "Fraca"
    
    print(f"\nForça da senha: {forca} ({pontos}/5)")
    
    return pontos >= 4

def testar_senhas():
    """Testa múltiplas senhas"""
    
    senhas_teste = ["123456", "MinhaSenh@123", "password", "S3nh@F0rt3!"]
    
    for senha in senhas_teste:
        print(f"\n{'='*40}")
        print(f"Teste: {senha}")
        print('='*40)
        validar_senha_completa(senha)

if __name__ == "__main__":
    testar_senhas()