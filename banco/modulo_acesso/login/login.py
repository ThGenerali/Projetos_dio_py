from banco.banco_dados import banco as bd
def login_conta(login, senha):
    global bd
    if login in bd and senha == bd[login]['senha']:
       conta = tuple(bd[login]['dado_conta'].items()) 
       print(f'Seja Bem vindo {login}')
       print(conta)