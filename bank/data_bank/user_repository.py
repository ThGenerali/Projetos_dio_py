from ..modulo_acao.conta import conta
#Verifcation data clients in database

bd = {}
def create_user(name, password, account_number, account_password):
    global bd
    bd.update({name:{'password':password, 'user_data':{'account_number':account_number, 'account_password':account_password}, 'account_data':{'balance':0, 'extrato':0}}})
    
    
def search_user(login, password):
    if login in bd:
        if password == bd[login]['password']: 
            return conta(login, bd[login]['user_data']['account_number'], bd[login]['user_data']['account_password'], bd[login]['account_data']['balance'], bd[login]['account_data']['extrato'])
        else:
            return 'incorreto'
    else:
        return False

def find_user(name, account_number):
    global bd
    if name in bd and account_number == bd[name]['user_data']['account_number']:
        return f'{name}\n {account_number}'
    else:
        return 'Conta não encontrada'

def update_transfer(name, account_number, value):
    global bd
    if name in bd and account_number == bd[name]['user_data']['account_number']:
        bd[name]['account_data']['balance'] += value
        return True
    else:
        return False
    
def update_balance(user, balance):
    global bd
    bd[user]['account_data']['balance'] = balance
    
    
def delete(user):
    global bd
    del bd[user]
    
def operate_verification(user, password):
    global bd
    if password == bd[user]['user_data']['account_password']:
        return 'Senha correta! Efetuando Operação...'
    else: 
        return 'password incorreta'
    
def account_verification(name):
    if name in bd:
        return True
    else:
        return False