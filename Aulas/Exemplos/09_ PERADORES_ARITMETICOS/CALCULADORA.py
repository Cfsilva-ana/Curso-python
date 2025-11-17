print("\n=== Calculadora Prática ===")

def calculadora_simples(num1, operador, num2):
    """Calculadora com todos os operadores"""
    
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero!"
    elif operador == "//":
        if num2 != 0:
            resultado = num1 // num2
        else:
            return "Erro: Divisão por zero!"
    elif operador == "%":
        if num2 != 0:
            resultado = num1 % num2
        else:
            return "Erro: Divisão por zero!"
    elif operador == "**":
        resultado = num1 ** num2
    else:
        return "Operador inválido!"
    
    return f"{num1} {operador} {num2} = {resultado}"

# Testando a calculadora
operacoes = [
    (15, "+", 7),
    (20, "-", 8),
    (6, "*", 9),
    (25, "/", 4),
    (17, "//", 5),
    (23, "%", 7),
    (3, "**", 4)
]

for num1, op, num2 in operacoes:
    resultado = calculadora_simples(num1, op, num2)
    print(resultado)