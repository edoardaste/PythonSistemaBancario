from services.DepositarService import deposito
from services.SaqueService import sacar
from services.ExtratoService import ExtratoService
from services.UsuarioService import CriarUsuario, filtrar_usuario
from services.ContaCorrente import ContaCorrenteService
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

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
contas = []
usuario = []

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        print(deposito(valor, saldo, extrato))

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor=valor, saldo=saldo, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        ExtratoService(saldo, extrato = extrato)
    
    elif opcao == "u":
        CriarUsuario(usuario)
        
    elif opcao == "c":
        numero_conta = len(contas) + 1
        verifica_conta = ContaCorrenteService(AGENCIA, numero_conta, usuario)
        
        if verifica_conta:
            contas.append(verifica_conta)
        
    elif opcao == "q":
        break
    
    else:
        print("Operação Invalida!")
