class ContaCorrente:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        
    def valida_cpf(self, cpf):
         return self.cpf.isdigit()
     