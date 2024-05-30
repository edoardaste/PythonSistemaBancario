
from services.ContaService import ContaService
from services.DepositarService import depositar
from services.ExtratoService import ExtratoService
from services.UsuarioService import CriarUsuario, filtrar_usuario



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
        print(depositar(usuario))

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        ContaService.sacar(usuario)

    elif opcao == "e":
        ExtratoService(saldo)
    
    elif opcao == "u":
        CriarUsuario(usuario)
        
    elif opcao == "c":
        numero_conta = len(contas) + 1
        verifica_conta = ContaService.ContaCorrenteService(contas, numero_conta, usuario)
        
        if verifica_conta:
            contas.append(verifica_conta)
        
    elif opcao == "q":
        break
    
    else:
        print("Operação Invalida!")
