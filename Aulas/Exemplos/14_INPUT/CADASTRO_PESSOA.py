print("=== Cadastro de Pessoa ===")

print("Vamos fazer seu cadastro!")

try:
    # Coletando dados
    nome = input("Nome completo: ").strip().title()
    idade = int(input("Idade: "))
    email = input("Email: ").strip().lower()
    salario = float(input("Salário: R$ "))
    
    # Validações básicas
    if idade < 0 or idade > 120:
        print("Idade inválida!")
    elif "@" not in email:
        print("Email inválido!")
    elif salario < 0:
        print("Salário inválido!")
    else:
        # Mostrando resultado
        print("\n" + "="*40)
        print("CADASTRO REALIZADO COM SUCESSO!")
        print("="*40)
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Email: {email}")
        print(f"Salário: R$ {salario:,.2f}")
        print("="*40)

except ValueError:
    print("Erro: Verifique os dados digitados!")