from interfaces.Transacao import Transacao
from model.Historico import Historico


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    