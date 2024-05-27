from model.Historico import Historico


class Conta:
    def __init__(self, cliente, numero):
        self._saldo =  0
        self._agencia = "0001"
        self._cliente = cliente
        self._numero = numero
        self._historico = Historico()
        
        
@classmethod
def nova_conta(cls, cliente, numero):
    return cls(numero, cliente)

@property
def saldo(self):
    return self._saldo

@property
def agencia(self):
    return self._agencia

@property
def historico(self):
    return self._historico

