from model.Conta import Conta
from services.UsuarioService import filtrar_usuario

def ContaCorrenteService(contas, numero, usuario): 
    conta = Conta(usuario, numero)
    cpf = input(print("Informe o CPF do usuário: "))
    cliente = filtrar_usuario(cpf, usuario)
 
    if cliente:
        print("Conta Criada com sucesso! ")
        return {"conta": conta, "usuario": usuario}
    
print("Usuário não encontrado!!")