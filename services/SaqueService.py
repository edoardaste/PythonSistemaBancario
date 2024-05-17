#function iniciada com * pois é keyword only, ou seja, especifica que a propriedade só poderá ser atribuida com uma key, ex name="name"
def sacar(*, valor, saldo, limite, numero_saques, LIMITE_SAQUES):
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saque = numero_saques > LIMITE_SAQUES

        if excedeu_limite:
           return print("Valor do limite excedido!")
            
        elif excedeu_saldo:
           return print("Valor do saque excedido!")
        
        elif excedeu_limite_saque:
           return  print("Excedeu limite de saque diário!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Extrato : R${valor:.2f}"

            numero_saques += 1
            return extrato, saldo
        else:
           return print("Valor não permitido!")