from ..banco_dados import UsuariosRepository
class conta:
    def __init__ (self, nome, numero_conta, senha_conta, saldo, extrato):
        self.nome = nome 
        self.numero_conta = numero_conta 
        self.senha_conta = senha_conta 
        self.saldo = saldo 
        self.extrato = extrato 
    
    def depositar():
        print('depositar')
    
    def sacar():
        print('sacando')
    
    def transferir():
        print('transferir')
    
    def acoes(self):
        opcao = 1
        while opcao != 0:
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
                    conta.depositar()
                case 2:
                    conta.sacar()
                case 3:
                    conta.transferir()
                case 0:
                    print('Saindo...')
                    break
                case _:
                    print('opção inválida')
     