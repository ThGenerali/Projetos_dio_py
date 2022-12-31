from ...banco_dados.UsuariosRepository import busca_cliente
def login_conta():
    
    logado = False
    while logado == False:
        login = input('digite seu usário: ')
        senha = input('digite sua senha: ')
        
        usuario = busca_cliente(login, senha)

        if usuario is None:
            print("Login ou senha incorretos, tente novamente.")
            logado = False
        else:
            logado = True
    
   
    
    

