# ============================================================
# 13. MÉTODO FORMAT (FORMATAÇÃO CLÁSSICA)
# ============================================================
# "texto {}".format(valor) - forma clássica
# Ainda muito usada em códigos antigos


nome = "Maria"
idade = 30
salario = 2500.75


print("\n=== Método format() ===")

# Formatação básica
print("Olá, eu sou {} e tenho {} anos".format(nome, idade))

# Com índices
print("Olá, eu sou {0} e tenho {1} anos".format(nome, idade))

# Com nomes
print("Olá, eu sou {nome} e tenho {idade} anos".format(nome=nome, idade=idade))

# Formatação de números
print("Salário: R$ {:.2f}".format(salario))
print("Salário: R$ {:,.2f}".format(salario))
