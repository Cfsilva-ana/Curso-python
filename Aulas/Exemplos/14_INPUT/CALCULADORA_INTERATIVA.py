print("=== Calculadora Interativa ===")

try:
    print("Vamos fazer um cálculo!")
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ").strip()
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            resultado = None
    else:
        print("Operação inválida!")
        resultado = None
    
    if resultado is not None:
        print(f"{num1} {operacao} {num2} = {resultado}")

except ValueError:
    print("Erro: Digite apenas números válidos!")