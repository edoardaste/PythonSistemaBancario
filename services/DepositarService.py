#positional only

def deposito(valor, saldo):
    
        if valor > 0:
            saldo += valor 
            print("Deposito Realizado!")

        else:
            print("Valor não permitido!")
