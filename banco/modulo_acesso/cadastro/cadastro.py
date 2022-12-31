from ...banco_dados.UsuariosRepository import AddUser
def cadastro_conta():
    print('''0
        Para te cadastrarmos
        solicitaremos as seguintes informações 
        ''')
    nome = input('Informe nome: ')
    senha = input('Informe uma senha de login: ')
    numero_conta = int(input('Informe um número para sua conta de 8 digitos: '))
    senha_conta = int(input('Informe uma senha para sua conta de 4 digitos: '))
   
    

    while len(str(numero_conta)) != 8:
        if len(str(numero_conta)) != 8:
            numero_conta = int(input('Número da conta não está dentro dos requisitos.\nPor favor digite um número de 8 digitos para sua conta: '))
        else:
            break
        
        while len(str(senha_conta)) != 4:
            if len(str(senha_conta)) != 4:
                senha_conta = int(input('Senha da conta não está dentro dos requisitos.\nPor favor digite uma senha de 4 digitos para sua conta: '))
            else:
                break
            
    
    AddUser(nome, senha, numero_conta, senha_conta)
    
          
    print('Conta cadastrada com sucesso!')

