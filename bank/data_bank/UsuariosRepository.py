from ..modulo_acao.conta import conta
#Verifcation data clients in database

bd = {}
def create_client(name, password, account_number, account_password):
    global bd
    bd.update({name:{'password':password, 'dado_cliente':{'account_number':account_number, 'account_password':account_password}, 'dado_conta':{'balance':0, 'extrato':0}}})
    
    
def search_client(login, password):
    if login in bd:
        if password == bd[login]['password']: 
            return conta(login, bd[login]['dado_cliente']['account_number'], bd[login]['dado_cliente']['account_password'], bd[login]['dado_conta']['saldo'], bd[login]['dado_conta']['extrato'])
        else:
            return 'incorreto'
    else:
        return False

def find_client(name, account_number):
    global bd
    if name in bd and account_number == bd[name]['dado_cliente']['account_number']:
        return f'{name}\n {account_number}'
    else:
        return 'Conta não encontrada'

def update_transfer(name, account_number, value):
    global bd
    if name in bd and account_number == bd[name]['dado_cliente']['account_number']:
        bd[name]['dado_conta']['saldo'] += value
        return True
    else:
        return False
    
def update_balance(usuary, balance):
    global bd
    bd[usuary]['dado_conta']['balance'] = balance
    
    
def delete(usuary):
    global bd
    del bd[usuary]
    
def verification_operation(usuary, password):
    global bd
    if password == bd[usuary]['dado_cliente']['account_password']:
        return 'Senha correta! Efetuando Operação...'
    else: 
        return 'password incorreta'
    
def verification_account(name):
    if name in bd:
        return True
    else:
        return False