#positional only

from model.Deposito import Deposito
from services.UsuarioService import filtrar_usuario


def depositar(cliente):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, cliente)

    if cliente:
        valor = float(input("Informe o valor do depósito: "))
        transacao = Deposito(valor)

    
