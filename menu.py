from services.DepositarService import deposito
from services.SaqueService import sacar
from services.ExtratoService import ExtratoService
from services.UsuarioService import CriarUsuario, filtrar_usuario
from services.ContaService import ContaCorrenteService
from model.ContaCorrente import ContaCorrente


menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato 
[u] - Criar Usuário
[c] - Criar Conta Corrente
[q] - Sair

=>
"""

contas = []
usuario = []
saldo = 0

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        print(deposito(valor, saldo))

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor=valor, saldo=saldo)

    elif opcao == "e":
        ExtratoService(saldo)
    
    elif opcao == "u":
        CriarUsuario(usuario)
        
    elif opcao == "c":
        numero_conta = len(contas) + 1
        verifica_conta = ContaCorrenteService(contas, numero_conta, usuario)
        
        if verifica_conta:
            contas.append(verifica_conta)
        
    elif opcao == "q":
        break
    
    else:
        print("Operação Invalida!")
