# VALIDADOR DE DADOS
# Exemplo prático usando vários operadores

def validar_usuario(nome, idade, email):
    """Valida dados do usuário usando vários operadores"""
    
    # Usando vários operadores
    nome_valido = nome and len(nome) >= 2
    idade_valida = isinstance(idade, int) and 0 <= idade <= 120
    email_valido = "@" in email and "." in email
    
    print(f"Nome '{nome}' válido: {nome_valido}")
    print(f"Idade {idade} válida: {idade_valida}")
    print(f"Email '{email}' válido: {email_valido}")
    
    return nome_valido and idade_valida and email_valido

def calculadora_avancada(a, operador, b):
    """Calculadora usando todos os operadores"""
    
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        return a / b if b != 0 else "Erro: Divisão por zero"
    elif operador == "//":
        return a // b if b != 0 else "Erro: Divisão por zero"
    elif operador == "%":
        return a % b if b != 0 else "Erro: Divisão por zero"
    elif operador == "**":
        return a ** b
    else:
        return "Operador inválido"

if __name__ == "__main__":
    # Testando validador
    print("=== Validador de Dados ===")
    resultado = validar_usuario("Ana", 25, "ana@email.com")
    print(f"Usuário válido: {resultado}")
    
    # Testando calculadora
    print("\n=== Calculadora Avançada ===")
    print(f"10 + 5 = {calculadora_avancada(10, '+', 5)}")
    print(f"10 / 3 = {calculadora_avancada(10, '/', 3)}")
    print(f"2 ** 8 = {calculadora_avancada(2, '**', 8)}")