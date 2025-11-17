# ============================================================
# TRY E EXCEPT - TRATAMENTO DE ERROS
# ============================================================
# Capturando e tratando exceções (erros) em Python

print("=== Tratamento de Erros ===")

# ============================================================
# 1. O QUE SÃO EXCEÇÕES?
# ============================================================
# Exceções são erros que ocorrem durante a execução
# Sem tratamento, elas param o programa

print("\n=== Sem Tratamento (programa para) ===")
# print(10 / 0)  # ZeroDivisionError - descomente para ver o erro
# print(int("abc"))  # ValueError - descomente para ver o erro


# ============================================================
# 2. TRY/EXCEPT BÁSICO
# ============================================================
# try: tenta executar o código
# except: executa se der erro

print("\n=== Try/Except Básico ===")

try:
    resultado = 10 / 0
    print(f"Resultado: {resultado}")
except:
    print("❌ Ops! Algo deu errado")

print("✅ Programa continua normalmente")


# ============================================================
# 3. CAPTURANDO ERROS ESPECÍFICOS
# ============================================================
# Melhor prática: capturar erros específicos

print("\n=== Erros Específicos ===")

try:
    numero = int("10")
    resultado = 10 / numero
    print(f"10 ÷ {numero} = {resultado}")
except ValueError:
    print("❌ Erro: Conversão inválida!")
except ZeroDivisionError:
    print("❌ Erro: Não é possível dividir por zero!")

print("✅ Programa continua")


# ============================================================
# 4. MÚLTIPLAS EXCEÇÕES
# ============================================================
# Capturando vários tipos de erro

print("\n=== Múltiplas Exceções ===")

try:
    lista = [1, 2, 3]
    indice = 1
    print(f"Elemento: {lista[indice]}")
except ValueError:
    print(" Digite um número válido!")
except IndexError:
    print(" Índice fora do alcance da lista!")
except Exception as e:
    print(f" Erro inesperado: {e}")


# ============================================================
# 5. CAPTURANDO A MENSAGEM DO ERRO
# ============================================================
# Usando 'as' para acessar detalhes do erro

print("\n=== Mensagem do Erro ===")

try:
    idade = 25
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    print(f"Você tem {idade} anos")
except ValueError as erro:
    print(f" Erro de valor: {erro}")
except Exception as erro:
    print(f" Erro geral: {erro}")


# ============================================================
# 6. ELSE E FINALLY
# ============================================================
# else: executa se NÃO houver erro
# finally: SEMPRE executa

print("\n=== Else e Finally ===")

try:
    numero = 16.0
    raiz = numero ** 0.5
except ValueError:
    print(" Número inválido!")
else:
    print(f" Raiz quadrada de {numero} = {raiz:.2f}")
finally:
    print(" Este bloco sempre executa")


# ============================================================
# 7. TIPOS COMUNS DE EXCEÇÕES
# ============================================================
print("\n=== Tipos Comuns de Exceções ===")

# ValueError - valor incorreto
try:
    int("abc")
except ValueError:
    print("ValueError: Conversão inválida")

# ZeroDivisionError - divisão por zero
try:
    10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Divisão por zero")

# IndexError - índice inválido
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("IndexError: Índice fora do alcance")

# KeyError - chave inexistente
try:
    dicionario = {"nome": "Ana"}
    print(dicionario["idade"])
except KeyError:
    print("KeyError: Chave não encontrada")

# TypeError - tipo incorreto
try:
    "texto" + 5
except TypeError:
    print("TypeError: Tipos incompatíveis")


# ============================================================
# 8. LEVANTANDO EXCEÇÕES PRÓPRIAS
# ============================================================
# Usando raise para criar seus próprios erros

print("\n=== Levantando Exceções ===")

def validar_idade(idade):
    if not isinstance(idade, int):
        raise TypeError("Idade deve ser um número inteiro")
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    if idade > 150:
        raise ValueError("Idade muito alta")
    return True

try:
    validar_idade(25)
    print("✅ Idade válida")
    
    validar_idade(-5)  # Vai dar erro
except ValueError as e:
    print(f" Erro de valor: {e}")
except TypeError as e:
    print(f" Erro de tipo: {e}")

