from ..modulo_acao.conta import conta


bd = {}
def adicionar_cliente(nome, senha, numero_conta, senha_conta):
    global bd
    bd.update({nome:{'senha':senha, 'dado_cliente':{'numero_conta':numero_conta, 'senha_conta':senha_conta}, 'dado_conta':{'saldo':0, 'extrato':0}}})
    print(bd)
    
def busca_cliente(login, senha):
    if login in bd and senha == bd[login]['senha']: 
        return conta(login, bd[login]['dado_cliente']['numero_conta'], bd[login]['dado_cliente']['senha_conta'], bd[login]['dado_conta']['saldo'], bd[login]['dado_conta']['extrato'])
    else:
        return 'incorreto'

def localizar_usuario():
    pass

def atualizar(usuario, saldo):
    global bd
    bd[usuario]['dado_conta']['saldo'] = saldo
    print(bd[usuario])
    
def excluir(usuario):
    global bd
    del bd[usuario]
    
def verificacao(usuario, senha):
    global bd
    if senha == bd[usuario]['dado_cliente']['senha_conta']:
        return 'Senha correta! Efetuando Operação...'
    else: 
        return 'senha incorreta'