#positional only

def deposito(valor, saldo, extrato):
    
        if valor > 0:
            saldo += valor 
            extrato += f"Extrato: R${valor:.2f}"
            return saldo, extrato

        else:
            print("Valor não permitido!")
