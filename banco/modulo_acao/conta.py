from ..banco_dados import UsuariosRepository
class conta:
    def __init__ (self, nome, numero_conta, senha_conta, saldo, extrato):
        self.nome = nome 
        self.numero_conta = numero_conta 
        self.senha_conta = senha_conta 
        self.saldo = saldo 
        self.extrato = extrato 
    
    def depositar(self):
        valor = int(input('Qual valor do depósito?\n'))
        senha_incorreta = True
        chances = 3
        while senha_incorreta == True:
            senha = int(input('Confirme a senha da sua conta: '))
            verificacao = UsuariosRepository.verificacao(self.nome, senha)
            if verificacao == 'senha incorreta':
                chances -= 1
                print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                if chances == 0:
                    print('Conta excluida')
                    UsuariosRepository.excluir(self.nome)
                    break 
            else:
                print(verificacao)
                self.saldo += valor 
                UsuariosRepository.atualizar(self.nome, self.saldo)
                print('Operação efetuada!')
                senha_incorreta = False
        
        
    def sacar(self):
        valor = int(input('Qual valor do saque?\n'))
        if valor <= self.saldo:
            senha_incorreta = True
            chances = 3
            while senha_incorreta == True:
                senha = int(input('Confirme a senha da sua conta: '))
                verificacao = UsuariosRepository.verificacao(self.nome, senha)
                if verificacao == 'senha incorreta':
                    chances -= 1
                    print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                    if chances == 0:
                        print('Conta excluida')
                        UsuariosRepository.excluir(self.nome)
                        break 
                else:
                    print(verificacao)
                    self.saldo -= valor 
                    UsuariosRepository.atualizar(self.nome, self.saldo)
                    print('Operação efetuada!')
                    senha_incorreta = False
        else:
            print('Saldo insuficiente para saque')
    
    def transferir(self):
        procura = False
        while procura == False:
            nome_usuario =  input('Informe o nome de quem você irá transferir: ')
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
            if valor > self.saldo:
                print('Valor de transferência negado.')
            else:
                senha_incorreta = True
                chances = 3
                while senha_incorreta == True:
                    senha = int(input('Confirme a senha da sua conta: '))
                    verificacao = UsuariosRepository.verificacao(self.nome, senha)
                    if verificacao == 'senha incorreta':
                        chances -= 1
                        print(f'você tem mais {chances} chances.\n (Caso erre todas as chances sua conta será excluida.)')
                        if chances == 0:
                            print('Conta excluida')
                            UsuariosRepository.excluir(self.nome)
                            break
                            
                    
                    else:
                        transferencia = UsuariosRepository.atualizar_transferencia(nome_usuario, conta_usuario, valor)
                        if transferencia == True:
                            print(verificacao)
                            self.saldo -= valor 
                            UsuariosRepository.atualizar(self.nome, self.saldo)
                            print('Operação efetuada!')
                            senha_incorreta = False
                            operacao = True
                        else:
                            print('Ocorreu um erro. por favor realize novamente a transferência.')
        
    def acoes(self):
        opcao = 1
        while opcao != 0:
            verificacao = UsuariosRepository.verificacao_conta(self.nome)
            if verificacao == True:
                opcao = int(input(f'''
                            Bem-vindo {self.nome}!
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
     