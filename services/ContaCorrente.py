from services.UsuarioService import filtrar_usuario

def ContaCorrenteService(agencia, conta, usuario): 
    cpf = input(print("Informe o CPF do usuário: "))
    cliente = filtrar_usuario(cpf, usuario)
 
    if cliente:
        print("Conta Criada com sucesso! ")
        return {"agencia": agencia, "conta": conta, "usuario": usuario}
    
print("Usuário não encontrado!!")