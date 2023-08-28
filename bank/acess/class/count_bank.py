from ..banco_dados import UsuariosRepository
class account:
    def __init__ (self, name, account_number, account_password, balance, statement):
        self.name = name 
        self.account_number = account_number 
        self.account_password = account_password 
        self.balance = balance 
        self.statement = statement 
    
    def depositar(self):
        valor = int(input('Qual valor do depósito?\n'))
        senha_incorreta = True
        chances = 3
        while senha_incorreta == True:
            password = int(input('Confirme a password da sua conta: '))
            verificacao = UsuariosRepository.verificacao(self.name, password)
            if verificacao == 'password incorreta':
                chances -= 1
                print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                if chances == 0:
                    print('Conta excluida')
                    UsuariosRepository.excluir(self.name)
                    break 
            else:
                print(verificacao)
                self.balance += valor 
                UsuariosRepository.atualizar(self.name, self.balance)
                print('Operação efetuada!')
                senha_incorreta = False
        
        
    def sacar(self):
        valor = int(input('Qual valor do saque?\n'))
        if valor <= self.balance:
            senha_incorreta = True
            chances = 3
            while senha_incorreta == True:
                password = int(input('Confirme a password da sua conta: '))
                verificacao = UsuariosRepository.verificacao(self.name, password)
                if verificacao == 'password incorreta':
                    chances -= 1
                    print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                    if chances == 0:
                        print('Conta excluida')
                        UsuariosRepository.excluir(self.name)
                        break 
                else:
                    print(verificacao)
                    self.balance -= valor 
                    UsuariosRepository.atualizar(self.name, self.balance)
                    print('Operação efetuada!')
                    senha_incorreta = False
        else:
            print('Saldo insuficiente para saque')
    
    def transferir(self):
        procura = False
        while procura == False:
            nome_usuario =  input('Informe o name de quem você irá transferir: ')
            conta_usuario = int(input('Informe o número da conta: '))
            localizar = UsuariosRepository.localizar_usuario(nome_usuario, conta_usuario)
            if localizar == 'Conta não encontrada':
                print(localizar)
            else:
                confirmacao = input(f'Você deseja transferir para {localizar}?\n (Digite "sim" para confirmar ou "não" para negar)\n')
                if confirmacao == 'sim':
                    procura = True
        
        operacao = False
        while operacao == False:
            valor = int(input('Qual valor de transferênica?\n'))
            if valor > self.balance:
                print('Valor de transferência negado.')
            else:
                senha_incorreta = True
                chances = 3
                while senha_incorreta == True:
                    password = int(input('Confirme a password da sua conta: '))
                    verificacao = UsuariosRepository.verificacao(self.name, password)
                    if verificacao == 'password incorreta':
                        chances -= 1
                        print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                        if chances == 0:
                            print('Conta excluida')
                            UsuariosRepository.excluir(self.name)
                            break
                            
                    
                    else:
                        transferencia = UsuariosRepository.atualizar_transferencia(nome_usuario, conta_usuario, valor)
                        if transferencia == True:
                            print(verificacao)
                            self.balance -= valor 
                            UsuariosRepository.atualizar(self.name, self.balance)
                            print('Operação efetuada!')
                            senha_incorreta = False
                            operacao = True
                        else:
                            print('Ocorreu um erro. por favor realize novamente a transferência.')
        
    def acoes(self):
        opcao = 1
        while opcao != 0:
            verificacao = UsuariosRepository.verificacao_conta(self.name)
            if verificacao == True:
                opcao = int(input(f'''
                            Bem-vindo {self.name}!
                            _____________________________
                                
                                1 - Depositar
                                2 - Sacar 
                                3 - Transferir
                                0 - Sair
                            _____________________________
                                
                            O que deseja fazer?\n
                            '''))
            
                match opcao:
                    case 1:    
                        conta.depositar(self)
                    case 2:       
                        conta.sacar(self)
                    case 3:
                        conta.transferir(self)
                    case 0:
                        print('Saindo...')
                        break
                    case _:
                        print('opção inválida')
            else:
                break
     