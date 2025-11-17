# VALIDADOR DE ENTRADA
# Exemplo prático de tratamento de erros

def obter_numero_valido():
    """Obtém um número válido do usuário"""
    
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("❌ Erro: Digite apenas números!")

def dividir_numeros():
    """Divide dois números com tratamento de erros"""
    
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        
        resultado = a / b
        print(f"✅ {a} ÷ {b} = {resultado}")
        
    except ValueError:
        print("❌ Erro: Digite apenas números!")
    except ZeroDivisionError:
        print("❌ Erro: Não é possível dividir por zero!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def validar_idade_completa():
    """Valida idade com múltiplas verificações"""
    
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        if idade > 150:
            raise ValueError("Idade muito alta")
            
        print(f"✅ Idade válida: {idade} anos")
        return idade
        
    except ValueError as erro:
        print(f"❌ Erro de valor: {erro}")
    except Exception as erro:
        print(f"❌ Erro geral: {erro}")

if __name__ == "__main__":
    print("=== Validador de Entrada ===")
    
    print("\n1. Obtendo número válido:")
    numero = obter_numero_valido()
    print(f"Número obtido: {numero}")
    
    print("\n2. Divisão com tratamento:")
    dividir_numeros()
    
    print("\n3. Validação de idade:")
    validar_idade_completa()