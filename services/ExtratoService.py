#positional only saldo, keyword only extrato
def ExtratoService(saldo, /, *, extrato):
     print("EXTRATO".center(10, "#"))
     print("Não foram realizadas movimentações" if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("------------------------------")
