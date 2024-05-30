from model.Cliente import Cliente
from model.PessoaFisica import PessoaFisica

def CriarUsuario(clientes):
  
  cpf = input("Informe o CPF: ")
  usuario = input(filtrar_usuario(cpf, clientes))
  verificacao = input("Deseja Criar um usuario? [s] - SIM [n] - NÃO")
  
  if usuario:
    print("Já existe um usuário com esse CPF!")
  elif verificacao == "s":
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
  else: 
    return quit

  cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
  
  clientes.append(cliente)
  
  print("Usuário criado")
    
    
def filtrar_usuario(cpf, clientes):
  usuarios_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else print("Usuário inexistente!")
  