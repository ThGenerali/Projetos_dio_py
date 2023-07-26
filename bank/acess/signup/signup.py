from ...banco_dados import UsuariosRepository 
def cadastro_conta():
    print('''
        Para te cadastrarmos
        solicitaremos as seguintes informações 
        ''')
    name = input('Informe nome: ')
    password = input('Informe uma senha de login: ')
    account_name = int(input('Informe um número para sua conta de 8 digitos: '))
    senha_conta = int(input('Informe uma senha para sua conta de 4 digitos: '))
   
    

    while len(str(account_name)) != 8:
        if len(str(account_name)) != 8:
            account_name = int(input('Número da conta não está dentro dos requisitos.\nPor favor digite um número de 8 digitos para sua conta: '))
        else:
            break
        
        while len(str(senha_conta)) != 4:
            if len(str(senha_conta)) != 4:
                senha_conta = int(input('Senha da conta não está dentro dos requisitos.\nPor favor digite uma senha de 4 digitos para sua conta: '))
            else:
                break
            
    
    UsuariosRepository.adicionar_cliente(name, password, account_name, senha_conta)
    
          
    print('Conta cadastrada com sucesso!')

