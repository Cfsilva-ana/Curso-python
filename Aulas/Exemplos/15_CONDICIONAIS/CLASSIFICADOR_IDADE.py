# CLASSIFICADOR DE IDADE
# Exemplo prático de condicionais

def classificar_idade():
    """Classifica pessoa por faixa etária"""
    
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 0:
            print("❌ Idade inválida!")
        elif idade <= 12:
            print("👶 Criança")
        elif idade <= 17:
            print("🧒 Adolescente")
        elif idade <= 59:
            print("👨 Adulto")
        elif idade <= 100:
            print("👴 Idoso")
        else:
            print("🎂 Centenário!")
            
    except ValueError:
        print("❌ Digite apenas números!")

if __name__ == "__main__":
    classificador_idade()