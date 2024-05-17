from model.Cliente import Cliente

def CriarUsuario(clientes):
  
  cpf = input("Informe o CPF: ")
  usuario = input(filtrar_usuario(cpf, clientes))
  
  if usuario:
    print("Já existe um usuário com esse CPF!")
  
  nome = input("Informe o nome: ")
  data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
  
  cliente = Cliente(nome, data_nascimento, endereco, cpf)
  
  clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
  
  return "Usuario criado"
    
    
def filtrar_usuario(cpf, clientes):
  usuarios_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None
  