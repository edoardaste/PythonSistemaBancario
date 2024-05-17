class Cliente:
    def __init__(self, nome, data_nascimento, endereco, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = cpf
        
    def valida_cpf(self, cpf):
         return self.cpf.isdigit()

        