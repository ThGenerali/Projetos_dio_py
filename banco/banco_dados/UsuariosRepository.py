from ..modulo_acao.conta import conta
bd = {}

def AddUser(nome, senha, numero_conta, senha_conta):
    global bd
    bd.update({nome:{'senha':senha, 'dado_cliente':{'numero_conta':numero_conta, 'senha_conta':senha_conta}, 'dado_conta':{'saldo':0, 'extrato':0}}})
    print(bd)
    
def busca_cliente(login, senha):
    if login in bd and senha == bd[login]['senha']: 
        conta( bd[login], bd[login]['dado_client']['numero_conta'], bd[login], bd[login]['dado_client']['senha_conta'], bd[login], bd[login]['dado_conta']['saldo'], bd[login]['dado_client']['senha_conta'], bd[login], bd[login]['dado_conta']['extrato'])
    return None
