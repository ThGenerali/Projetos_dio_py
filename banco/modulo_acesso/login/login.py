from ...banco_dados import UsuariosRepository
from ...modulo_acao.conta import conta

def login_conta():   
    logado = False
    while logado == False:
        login = input('digite seu usário: ')
        senha = input('digite sua senha: ')
        
        usuario = UsuariosRepository.busca_cliente(login, senha)

        if usuario is 'incorreto':
            print("Login ou senha incorretos, tente novamente.")
            logado = False
        else:
            logado = True 
    usuario.acoes()
        
   
    
    

