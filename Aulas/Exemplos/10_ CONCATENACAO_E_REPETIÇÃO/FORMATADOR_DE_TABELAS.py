print("\n=== Formatador de Tabelas ===")

def criar_tabela(dados, cabecalhos):
    """Cria uma tabela formatada"""
    
    # Calcular largura das colunas
    larguras = []
    for i, cabecalho in enumerate(cabecalhos):
        largura_max = len(cabecalho)
        for linha in dados:
            largura_max = max(largura_max, len(str(linha[i])))
        larguras.append(largura_max + 2)  # +2 para espaçamento
    
    # Criar linha separadora
    separador = "+" + "+".join(["-" * largura for largura in larguras]) + "+"
    
    # Criar cabeçalho
    tabela = separador + "\n"
    linha_cabecalho = "|"
    for i, cabecalho in enumerate(cabecalhos):
        linha_cabecalho += f" {cabecalho:<{larguras[i]-1}}|"
    tabela += linha_cabecalho + "\n" + separador + "\n"
    
    # Criar linhas de dados
    for linha in dados:
        linha_dados = "|"
        for i, valor in enumerate(linha):
            linha_dados += f" {str(valor):<{larguras[i]-1}}|"
        tabela += linha_dados + "\n"
    
    tabela += separador
    return tabela

# Testando a tabela
dados_vendas = [
    ["Notebook", "R$ 2.500,00", "5"],
    ["Mouse", "R$ 45,00", "20"],
    ["Teclado", "R$ 120,00", "15"]
]

cabecalhos_vendas = ["Produto", "Preço", "Estoque"]
tabela_vendas = criar_tabela(dados_vendas, cabecalhos_vendas)
print(tabela_vendas)