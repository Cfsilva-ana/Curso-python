from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///SQLALCHEMY/dados.db')
Base = declarative_base()
_Sessao = sessionmaker(engine)

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True) 
    nome = Column(String(50), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<{self.nome}>"

Base.metadata.create_all(engine) 

while True:
    opcao = input('\nO que deseja fazer?\n1 - Adicionar usuário\n2 - Deletar usuário\n3 - Ver usuários\n4 - Sair\nEscolha: ')
    
    if opcao == '4':
        break

    elif opcao == '1':
        with _Sessao() as sessao:
            input_nome = input('Digite o nome do usuário: ')
            input_idade = int(input('Digite a idade do usuário: '))
            sessao.add(Usuario(nome=input_nome, idade=input_idade))
            sessao.commit()
            print('Usuário adicionado!')

    elif opcao == '2':
        with _Sessao() as sessao:
            op_1 = input('Deseja deletar um usuário por ID ou nome? (ID/nome): ')
            
            if op_1 == 'ID':
                input_id = int(input('Digite o ID do usuário: '))
                usuario = sessao.query(Usuario).filter_by(id=input_id).first()
                if usuario:
                    sessao.delete(usuario)
                    sessao.commit()
                    print('Usuário deletado!')
                else:
                    print('Usuário não encontrado!')

            elif op_1 == 'nome':
                input_nome = input('Digite o nome do usuário: ')
                usuario = sessao.query(Usuario).filter_by(nome=input_nome).first()
                if usuario:
                    sessao.delete(usuario)
                    sessao.commit()
                    print('Usuário deletado!')
                else:
                    print('Usuário não encontrado!')

    elif opcao == '3':
        with _Sessao() as sessao:
            usuarios = sessao.query(Usuario).all()
            if usuarios:
                for usuario in usuarios:
                    print(f'ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.idade}')
            else:
                print('Nenhum usuário encontrado.')

    else:
        print('Opção inválida')   