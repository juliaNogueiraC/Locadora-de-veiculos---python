

def menu():
    print("------------------------------------------------")
    print("|        SISTEMA DE LOCAÇÃO DE VEICULOS         |")
    print("|             Cadastro de veiculo               |")
    print(" -----------------------------------------------")
    print("   1- Inserir cadastro de aluguel")
    print("   2- Listar os cadastros registrados no sistema")
    print("   3- Buscar um cadastro ")
    print("   4- excluir um cadastro")
    print(" ----------------------------------------------")
    print(" ----------------------------------------------")
    print("   0- Sair do programa")
    print(" ----------------------------------------------")
    print(" ----------------------------------------------")
    opcao = input()
    return opcao

#--------------------------------------------------------
def busca(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
              return i
    return -1
#---------------------------------------------------------
def cadastroVeiculo(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_nome,prazoIn,prazoFim,valortot):
    v_codigo = input("Informe o código do veiculo a ser alugado: ")
    c_nome = input("Informe o nome do cliente que vai alugar: ")
    prazoInicial = input("informe a data inicial:")
    prazoFinal = input("informe o prazo para devolução:")

    if busca(veiculos_codigo,v_codigo) == -1:

      v_modelo = input("Informe o modelo: ")
      v_ano = int(input("Informe o ano de fabricação: "))
      valor = input("Informe o valor a ser pago para a utilização desse veiculo durante esse prazo")
      clientes_nome.append(c_nome)
      veiculos_codigo.append(v_codigo)
      veiculos_modelo.append(v_modelo)
      veiculos_ano.append(v_ano)
      prazoIn.append(prazoInicial)
      prazoFim.append(prazoFinal)
      valortot.append(valor)
      print("\n o cliente " + c_nome + " realizou a locação do Veiculo de código: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano) + ", alugado dia " + prazoInicial + "para a devolução na data de " + prazoFinal + "pelo valor total de " + valor + ".")
    else:
        print("Código " + v_codigo + " já está cadastrado!")
#--------------------------------------------------
def todosOsVeiculos(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_nome,prazoIn,prazoFim,valortot):
    if len(veiculos_codigo) > 0:
      for i in range(len(veiculos_codigo)):
        v_codigo = veiculos_codigo[i]
        v_modelo = veiculos_modelo[i]
        v_ano = veiculos_ano[i]
        c_nome = clientes_nome[i]
        prazoInicial = prazoIn[i]
        prazoFinal = prazoFim[i]
        valor = valortot[i]
        print("\n CADASTRO: cliente: " + c_nome + " , código: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano) + ", data de locação: " + prazoInicial + ", Data de devolução: " + prazoFinal + ", valor total: " + valor + ".")
    else:
        print("Não há cadastro a serem listados!")
#--------------------------------------------------
def buscarVeiculo(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_nome,prazoIn,prazoFim,valortot):
    codigo_pesquisar = input("Informe o código do veiculo a ser pesquisado: ")
    indice = busca(veiculos_codigo, codigo_pesquisar)
    if indice != -1:
        v_codigo = veiculos_codigo[indice]
        v_modelo = veiculos_modelo[indice]
        v_ano = veiculos_ano[indice]
        c_nome = clientes_nome[indice]
        prazoInicial = prazoIn[indice]
        prazoFinal = prazoFim[indice]
        valor = valortot[indice]
        print("\nVeiculo código: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano) + " alugado para o cliente" + c_nome + " na data de " + prazoInicial + " até o prazo de " + prazoFinal + " pelo valor total de " + valor + ".")
    else:
        print("\nVeiculo de código " + codigo_pesquisar + " não encontrado!")

#--------------------------------------------------
# remove deslocando os elementos
def remover1(lista, indice):
    i = indice
    while i < len(lista) - 1:
          lista[i] = lista[i + 1]
          i = i + 1
    lista.pop()

# remove colocando o ultimo elemento na posicao que eu quero remover
def remover2(lista, indice):
    ultimo_indice = len(lista) - 1
    lista[indice] = lista[ultimo_indice]
    lista.pop()
#--------------------------------------------------
def excluirVeiculo(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_nome,prazoIn,prazoFim,valortot):
    codigo_remover = input("Informe o código do veiculo a ser removido: ")
    indice = busca(veiculos_codigo, codigo_remover)
    if indice != -1:
        remover2(veiculos_codigo, indice)
        remover2(veiculos_modelo, indice)
        remover2(veiculos_ano, indice)
        remover2(clientes_nome,indice)
        remover2(prazoIn,indice)
        remover2(prazoFim, indice)
        remover2(valortot, indice)
        print("cadstro removido com sucesso!")
    else:
        print("\nVeiculo de código " + codigo_remover + " não encontrado!")



def main():
    # veiculo
    veiculos_codigo = []
    veiculos_modelo = []
    veiculos_ano = []


    # clientes
    clientes_cpf = []
    clientes_nome = []
    clientes_ano = []

    # aluguel
    prazoIn = []
    prazoFim = []
    valortot = []



   # loop das informações que aparecem no menu
    opção = 'x'
    while opção != '0':
          opção = menu()
          if opção == '1':
              cadastroVeiculo(veiculos_codigo,veiculos_modelo,veiculos_ano, clientes_nome,prazoIn,prazoFim,valortot)
          elif opção == '2':
              todosOsVeiculos(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_nome,prazoIn,prazoFim,valortot)
          elif opção == '3':
              buscarVeiculo(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_nome,prazoIn,prazoFim,valortot)
          elif opção == '4':
              excluirVeiculo(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_nome,prazoIn,prazoFim,valortot)
          elif opção == '0':
              print("saindo do sistema......")


import datetime
main()