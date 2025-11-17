print("\n=== Exemplo Prático ===")

# Dados de uma pessoa
pessoa = {
    "nome": "Maria Santos",      # str
    "idade": 28,                 # int
    "altura": 1.68,              # float
    "peso": 65.0,                # float
    "ativa": True,               # bool
    "salario": 4500.50           # float
}

# Processando os dados
print("FICHA PESSOAL")
print("=" * 30)

for chave, valor in pessoa.items():
    tipo = type(valor).__name__
    
    if tipo == 'str':
        valor_formatado = valor.title()
    elif tipo == 'float' and chave == 'salario':
        valor_formatado = f"R$ {valor:,.2f}"
    elif tipo == 'float':
        valor_formatado = f"{valor:.2f}"
    elif tipo == 'bool':
        valor_formatado = "Sim" if valor else "Não"
    else:
        valor_formatado = valor
    
    print(f"{chave.title()}: {valor_formatado} ({tipo})")

# Cálculos adicionais
imc_pessoa = pessoa["peso"] / (pessoa["altura"] ** 2)
print(f"\nIMC: {imc_pessoa:.1f} (calculado)")

if imc_pessoa < 18.5:
    classificacao = "Abaixo do peso"
elif imc_pessoa < 25:
    classificacao = "Peso normal"
else:
    classificacao = "Acima do peso"

print(f"Classificação: {classificacao}")