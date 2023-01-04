from ..modulo_acao.conta import conta

bd = {}

def Aicionar_cliente(nome, senha, numero_conta, senha_conta):
    global bd
    bd.update({nome:{'senha':senha, 'dado_cliente':{'numero_conta':numero_conta, 'senha_conta':senha_conta}, 'dado_conta':{'saldo':0, 'extrato':0}}})
    print(bd)
    
def busca_cliente(login, senha):
    if login in bd and senha == bd[login]['senha']: 
        return conta(login, bd[login]['dado_cliente']['numero_conta'], bd[login]['dado_cliente']['senha_conta'], bd[login]['dado_conta']['saldo'], bd[login]['dado_conta']['extrato'])
    else:
        return 'incorreto'

def localizar_cliente():
    pass
def atualizar():
    pass
def excluir():
    pass