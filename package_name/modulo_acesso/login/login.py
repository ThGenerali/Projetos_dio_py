def teste(login, senha):
    dados = {'araujo':{'senha':'hito', 'dado_cliente':{'numero_conta':98745, 'senha_conta':1904}, 'dado_conta':{'saldo':1500, 'extrato':''}},
             'araea':{'senha':'hitorie', 'dado_cliente':{'numero_conta':98745, 'senha_conta':1904}, 'dado_conta':{'saldo':1500, 'extrato':''}}}
    if login in dados and senha == dados[login]['senha']:
       conta = tuple(dados[login]['dado_conta'].items()) 
       print(f'Seja Bem vindo {login}')
       print(conta)