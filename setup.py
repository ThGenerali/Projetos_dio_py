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

    if escolha == 1:
        login.login_conta()
        
    if escolha == 2:
        cadastro.cadastro_conta()
        
        
print(bd)