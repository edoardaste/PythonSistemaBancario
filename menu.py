menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato 
[q] - Sair

=>
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Extrato: R${valor:.2f}"

        else:
            print("Valor não permitido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saque = numero_saques > LIMITE_SAQUES

        if excedeu_limite:
             print("Valor do limite excedido!")
            
        elif excedeu_saldo:
             print("Valor do saque excedido!")
        
        elif excedeu_limite_saque:
             print("Excedeu limite de saque diário!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Extrato : R${valor:.2f}"

            numero_saques += 1
        else:
            print("Valor não permitido!")


    elif opcao == "e":
        extrato_msg = "EXTRATO"
        print(extrato_msg.center(10, "#"))
        print(f"\nSaldo: R$ {saldo:.2f}")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação Invalida!")
