from interfaces.Transacao import Transacao
from model.Historico import Historico
from services.SaqueService import sacar


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = sacar(self.valor)
        
        if sucesso:
            Historico.adicionar_transacao(self)