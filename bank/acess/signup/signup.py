from ...data_bank import user_repository
def cadastro_conta():
    print('''
        Para te cadastrarmos
        solicitaremos as seguintes informações 
        ''')
    name = input('Informe nome: ')
    password = input('Informe uma senha de login: ')
    number_account = int(input('Informe um número para sua conta de 8 digitos: '))
    password_account = int(input('Informe uma senha para sua conta de 4 digitos: '))
   
    

    while len(str(number_account)) != 8:
        if len(str(number_account)) != 8:
            number_account = int(input('Número da conta não está dentro dos requisitos.\nPor favor digite um número de 8 digitos para sua conta: '))
        else:
            break
        
        while len(str(password_account)) != 4:
            if len(str(password_account)) != 4:
                password_account = int(input('Senha da conta não está dentro dos requisitos.\nPor favor digite uma senha de 4 digitos para sua conta: '))
            else:
                break
            
    
    user_repository.adicionar_cliente(name, password, number_account, password_account)
    
          
    print('Conta cadastrada com sucesso!')

