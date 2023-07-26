from ..modulo_acao.conta import conta
#Verifcation data clients in database

bd = {}
def adicionar_cliente(nome, senha, numero_conta, senha_conta):
    global bd
    bd.update({nome:{'senha':senha, 'dado_cliente':{'numero_conta':numero_conta, 'senha_conta':senha_conta}, 'dado_conta':{'saldo':0, 'extrato':0}}})
    
    
def busca_cliente(login, senha):
    if login in bd:
        if senha == bd[login]['senha']: 
            return conta(login, bd[login]['dado_cliente']['numero_conta'], bd[login]['dado_cliente']['senha_conta'], bd[login]['dado_conta']['saldo'], bd[login]['dado_conta']['extrato'])
        else:
            return 'incorreto'
    else:
        return False

def localizar_usuario(nome, numero_conta):
    global bd
    if nome in bd and numero_conta == bd[nome]['dado_cliente']['numero_conta']:
        return f'{nome}\n {numero_conta}'
    else:
        return 'Conta não encontrada'

def atualizar_transferencia(nome, numero_conta, valor):
    global bd
    if nome in bd and numero_conta == bd[nome]['dado_cliente']['numero_conta']:
        bd[nome]['dado_conta']['saldo'] += valor
        return True
    else:
        return False
    
def atualizar(usuario, saldo):
    global bd
    bd[usuario]['dado_conta']['saldo'] = saldo
    
    
def excluir(usuario):
    global bd
    del bd[usuario]
    
def verificacao(usuario, senha):
    global bd
    if senha == bd[usuario]['dado_cliente']['senha_conta']:
        return 'Senha correta! Efetuando Operação...'
    else: 
        return 'senha incorreta'
    
def verificacao_conta(nome):
    if nome in bd:
        return True
    else:
        return False