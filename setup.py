from banco.modulo_acesso.cadastro import cadastro
from banco.modulo_acesso.login import login
from banco.banco_dados.UsuariosRepository import bd
escolha = 0
while escolha != 3:
    escolha = int(input('''
                    Olá! Bem-vindo ao banco GENERALI
                    ________________________________
                    1 - Entrar
                    2 - Cadastrar
                    3 - Encerrar
                    ________________________________
                    O que você deseja?
                    '''))

    match escolha:
        
        case 1:
            login.login_conta()
        
        case 2:
            cadastro.cadastro_conta()
        
        case 3:
            print('Encerrando...')
            break
        
        case _:
            print('Opção inválida')
            
    
print('Banco encerrado. Até mais!')

