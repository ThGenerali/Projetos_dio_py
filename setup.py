from package_name.modulo_acesso.login import cteste
escolha = int(input('''
                Olá! Bem-vindo ao banco GENERALI
                ________________________________
                1 - Login
                2 - Cadastrar
                3 - Encerrar
                ________________________________
                O que você deseja?
                '''))

if escolha == 1:
    login = input('digite seu usário: ')
    senha = input('digite sua senha: ')
    cteste.teste(login, senha)