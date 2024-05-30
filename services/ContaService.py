from model.Conta import Conta
from model.ContaCorrente import ContaCorrente
from model.Saque import Saque
from services.UsuarioService import filtrar_usuario

class ContaService:
    
    def ContaCorrenteService(cliente, numero_conta, contas): 
        cpf = input("Informe o CPF do cliente: ")
        cliente = filtrar_usuario(cpf, cliente)

        if not cliente:
            print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
            return
        conta = ContaCorrente(cliente=cliente, conta=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)

        print("\n=== Conta criada com sucesso! ===")
            
    
    def sacar(self, valor):
            numero_saques = len(
                [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
            )

            excedeu_limite = valor > self.limite
            excedeu_saques = numero_saques >= self.limite_saques

            if excedeu_limite:
                print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

            elif excedeu_saques:
                print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

            else:
                return super().sacar(valor)

            return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """
            
    
        