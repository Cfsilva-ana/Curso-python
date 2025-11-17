print("=== Sistema de Login ===")

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