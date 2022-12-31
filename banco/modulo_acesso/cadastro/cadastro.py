
bd = {}
def cadastro_conta():
    global bd
    print('''
        Para te cadastrarmos
        solicitaremos as seguintes informações 
        ''')
    usuario = input('Informe nome: ')
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
            
    
    bd.update({usuario:{'senha':senha, 'dado_cliente':{'numero_conta':numero_conta, 'senha_conta':senha_conta}, 'dado_conta':{'saldo':0, 'extrato':0}}})      
    print('Conta cadastrada com sucesso!')

cadastro_conta()
print(bd)
cadastro_conta()
print(bd)