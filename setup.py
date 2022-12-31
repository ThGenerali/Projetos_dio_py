from banco.modulo_acesso.cadastro.cadastro import cadastro_conta
from dio.projetos.projeto_banco.Projetos_dio_py.banco.modulo_acesso.login.login import login_conta

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
    login = input('digite seu usário: ')
    senha = input('digite sua senha: ')
    login_conta(login, senha)
    
if escolha ==2:
    cadastro_conta()