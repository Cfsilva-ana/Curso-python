# ============================================================
# LOOPS WHILE - REPETIÇÕES
# ============================================================
# Executando código repetidamente enquanto uma condição for verdadeira

print("=== Loops While ===")

# ============================================================
# 1. CONCEITO BÁSICO DO WHILE
# ============================================================
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

print("=== While Básico ===")

# Exemplo simples
contador = 0
print("Contando até 5:")

while contador < 5:
    print(f"Contador: {contador}")
    contador = contador + 1  # Incrementa para evitar loop infinito

print("Fim da contagem")


# ============================================================
# 2. CUIDADO COM LOOPS INFINITOS
# ============================================================
print("\n=== Evitando Loops Infinitos ===")

# ❌ CUIDADO: Este seria um loop infinito
# while True:
#     print("Isso nunca para!")  # NÃO execute isso!

# ✅ CORRETO: Sempre tenha uma condição de saída
contador = 0
while contador < 3:
    print(f"Execução {contador + 1}")
    contador += 1  # IMPORTANTE: sempre modifique a variável de controle


# ============================================================
# 3. USANDO BREAK PARA SAIR DO LOOP
# ============================================================
print("\n=== Usando break ===")

# Loop com break
while True:
    nome = input("Digite seu nome (ou 'sair' para terminar): ")
    
    if nome.lower() == 'sair':
        break  # Sai do loop
    
    print(f"Olá, {nome}!")

print("Programa encerrado!")


# ============================================================
# 4. USANDO CONTINUE PARA PULAR ITERAÇÕES
# ============================================================
print("\n=== Usando continue ===")

contador = 0
while contador < 10:
    contador += 1
    
    # Pula números pares
    if contador % 2 == 0:
        continue  # Volta para o início do loop
    
    print(f"Número ímpar: {contador}")


# ============================================================
# 5. CONTADOR CRESCENTE E DECRESCENTE
# ============================================================
print("\n=== Contadores ===")

# Contador crescente
print("Crescente:")
i = 1
while i <= 5:
    print(f"i = {i}")
    i += 1

# Contador decrescente
print("\nDecrescente:")
j = 5
while j >= 1:
    print(f"j = {j}")
    j -= 1


# ============================================================
# 6. VALIDAÇÃO DE ENTRADA COM WHILE
# ============================================================
print("\n=== Validação de Entrada ===")

def obter_idade_valida():
    """Obtém uma idade válida do usuário"""
    
    while True:
        try:
            idade = int(input("Digite sua idade (0-120): "))
            
            if 0 <= idade <= 120:
                return idade
            else:
                print("❌ Idade deve estar entre 0 e 120 anos!")
                
        except ValueError:
            print("❌ Digite apenas números inteiros!")

# Descomente para testar
# idade_valida = obter_idade_valida()
# print(f"✅ Idade válida: {idade_valida} anos")


# ============================================================
# 7. MENU INTERATIVO COM WHILE
# ============================================================
print("\n=== Menu Interativo ===")

def menu_principal():
    """Menu principal do programa"""
    
    while True:
        print("\n" + "="*30)
        print("MENU PRINCIPAL")
        print("="*30)
        print("1. Calculadora")
        print("2. Conversor de temperatura")
        print("3. Contador")
        print("0. Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("🧮 Abrindo calculadora...")
        elif opcao == "2":
            print("🌡️ Abrindo conversor...")
        elif opcao == "3":
            print("🔢 Abrindo contador...")
        elif opcao == "0":
            print("👋 Saindo do programa...")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

# Descomente para testar
# menu_principal()


# ============================================================
# 8. EXEMPLO PRÁTICO: CALCULADORA COM WHILE
# ============================================================
print("\n=== Calculadora com While ===")

def calculadora_completa():
    """Calculadora que funciona até o usuário querer sair"""
    
    print("🧮 Calculadora iniciada!")
    
    while True:
        print("\n" + "-"*40)
        
        # Entrada dos números
        try:
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /): ").strip()
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")
            continue
        
        # Validação do operador
        if operador not in ['+', '-', '*', '/']:
            print("❌ Operador inválido! Use +, -, * ou /")
            continue
        
        # Cálculo
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                print("❌ Erro: Divisão por zero!")
                continue
            resultado = num1 / num2
        
        # Resultado
        print(f"✅ {num1} {operador} {num2} = {resultado}")
        
        # Pergunta se quer continuar
        continuar = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
        if continuar.startswith('n'):
            print("👋 Calculadora encerrada!")
            break

# Descomente para testar
# calculadora_completa()


# ============================================================
# 9. EXEMPLO PRÁTICO: JOGO DE ADIVINHAÇÃO
# ============================================================
print("\n=== Jogo de Adivinhação ===")

def jogo_adivinhacao():
    """Jogo onde o usuário tenta adivinhar um número"""
    
    import random
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 7
    
    print("🎮 Jogo de Adivinhação!")
    print(f"Adivinhe o número entre 1 e 100 (você tem {max_tentativas} tentativas)")
    
    while tentativas < max_tentativas:
        try:
            palpite = int(input(f"\nTentativa {tentativas + 1}: "))
            tentativas += 1
            
            if palpite == numero_secreto:
                print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
                break
            elif palpite < numero_secreto:
                print("📈 Muito baixo! Tente um número maior.")
            else:
                print("📉 Muito alto! Tente um número menor.")
            
            # Mostrar tentativas restantes
            restantes = max_tentativas - tentativas
            if restantes > 0:
                print(f"Tentativas restantes: {restantes}")
            
        except ValueError:
            print("❌ Digite apenas números!")
            tentativas -= 1  # Não conta como tentativa válida
    
    if tentativas >= max_tentativas:
        print(f"😞 Suas tentativas acabaram! O número era {numero_secreto}")

# Descomente para testar
# jogo_adivinhacao()


# ============================================================
# 10. EXEMPLO PRÁTICO: SISTEMA DE LOGIN
# ============================================================
print("\n=== Sistema de Login ===")

def sistema_login():
    """Sistema de login com tentativas limitadas"""
    
    usuario_correto = "admin"
    senha_correta = "123456"
    max_tentativas = 3
    tentativas = 0
    
    print("🔐 Sistema de Login")
    
    while tentativas < max_tentativas:
        print(f"\nTentativa {tentativas + 1} de {max_tentativas}")
        
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        if usuario == usuario_correto and senha == senha_correta:
            print("✅ Login realizado com sucesso!")
            print("🎉 Bem-vindo ao sistema!")
            break
        else:
            tentativas += 1
            restantes = max_tentativas - tentativas
            
            if restantes > 0:
                print(f"❌ Credenciais incorretas! Tentativas restantes: {restantes}")
            else:
                print("🚫 Acesso bloqueado! Muitas tentativas incorretas.")

# Descomente para testar
# sistema_login()


# ============================================================
# 11. DICAS IMPORTANTES
# ============================================================
print("\n=== Dicas Importantes ===")

print("💡 Dicas sobre while:")
print("1. Sempre tenha uma condição de saída")
print("2. Modifique a variável de controle dentro do loop")
print("3. Use break para sair do loop")
print("4. Use continue para pular iterações")
print("5. Cuidado com loops infinitos")
print("6. Valide entradas do usuário")

# Exemplo de boas práticas
print("\n✅ Exemplo de bom while:")
contador = 0
while contador < 3:
    print(f"Iteração {contador}")
    contador += 1  # SEMPRE modifique a variável de controle


print("\n🎉 Você dominou loops while!")