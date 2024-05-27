#function iniciada com * pois é keyword only, ou seja, especifica que a propriedade só poderá ser atribuida com uma key, ex name="name"
def sacar(*, valor, saldoS):
    
        excedeu_saldo = valor > saldo
            
        if excedeu_saldo:
           return print("Valor do saque excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Extrato : R${valor:.2f}"

            numero_saques += 1
            return extrato, saldo
        else:
           return print("Valor não permitido!")