from ..banco_dados import user_repository
class account:
    def __init__ (self, name, account_number, account_password, balance, statement):
        self.name = name 
        self.account_number = account_number 
        self.account_password = account_password 
        self.balance = balance 
        self.statement = statement 
    
    def deposit(self):
        value = int(input('Qual value do depósito?\n'))
        wrong_password = True
        chances = 3
        while wrong_password == True:
            password = int(input('Confirme a password da sua conta: '))
            verification = user_repository.operate_verification(self.name, password)
            if verification == 'password incorreta':
                chances -= 1
                print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                if chances == 0:
                    print('Conta excluida')
                    user_repository.delete(self.name)
                    break 
            else:
                print(verification)
                self.balance += value 
                user_repository.update_balance(self.name, self.balance)
                print('Operação efetuada!')
                wrong_password = False
        
        
    def draw(self):
        value = int(input('Qual value do saque?\n'))
        if value <= self.balance:
            wrong_password = True
            chances = 3
            while wrong_password == True:
                password = int(input('Confirme a password da sua conta: '))
                verification = user_repository.operate_verification(self.name, password)
                if verification == 'password incorreta':
                    chances -= 1
                    print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                    if chances == 0:
                        print('Conta excluida')
                        user_repository.delete(self.name)
                        break 
                else:
                    print(verification)
                    self.balance -= value 
                    user_repository.update_balance(self.name, self.balance)
                    print('Operação efetuada!')
                    wrong_password = False
        else:
            print('Saldo insuficiente para saque')
    
    def transfer(self):
        procura = False
        while procura == False:
            nome_usuario =  input('Informe o name de quem você irá transfer: ')
            conta_usuario = int(input('Informe o número da conta: '))
            localizar = user_repository.find_user(nome_usuario, conta_usuario)
            if localizar == 'Conta não encontrada':
                print(localizar)
            else:
                confirmacao = input(f'Você deseja transfer para {localizar}?\n (Digite "sim" para confirmar ou "não" para negar)\n')
                if confirmacao == 'sim':
                    procura = True
        
        operacao = False
        while operacao == False:
            value = int(input('Qual value de transferênica?\n'))
            if value > self.balance:
                print('Valor de transferência negado.')
            else:
                wrong_password = True
                chances = 3
                while wrong_password == True:
                    password = int(input('Confirme a password da sua conta: '))
                    verification = user_repository.operate_verification(self.name, password)
                    if verification == 'password incorreta':
                        chances -= 1
                        print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                        if chances == 0:
                            print('Conta excluida')
                            user_repository.delete(self.name)
                            break
                            
                    
                    else:
                        transferencia = user_repository.update_transfer(nome_usuario, conta_usuario, value)
                        if transferencia == True:
                            print(verification)
                            self.balance -= value 
                            user_repository.update_balance(self.name, self.balance)
                            print('Operação efetuada!')
                            wrong_password = False
                            operacao = True
                        else:
                            print('Ocorreu um erro. por favor realize novamente a transferência.')
        
    def actions(self):
        opcao = 1
        while opcao != 0:
            verification = user_repository.account_verification(self.name)
            if verification == True:
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
                        conta.deposit(self)
                    case 2:       
                        conta.draw(self)
                    case 3:
                        conta.transfer(self)
                    case 0:
                        print('Saindo...')
                        break
                    case _:
                        print('opção inválida')
            else:
                break
     