from model.Cliente import Cliente


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, endereco, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
    def valida_cpf(self, cpf):
         return self.cpf.isdigit()

        