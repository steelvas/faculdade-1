from Cliente import Cliente
from Produto import Produto
from Pedido import Pedido

produtos = []
clientes = []
pedidos = []


def menu():
    while True:
        print("\n=== Coffee Shops Tia Rosa ===")
        print("1. Cadastrar produto")
        print("2. Cadastrar cliente")
        print("3. Fazer pedido")
        print("4. Ver produtos")
        print("5. Ver clientes")
        print("6. Ver pedidos")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            cadastrar_cliente()
        elif escolha == '3':
            fazer_pedido()
        elif escolha == '4':
            listar_produtos()
        elif escolha == '5':
            listar_clientes()
        elif escolha == '6':
            listar_pedidos()
        elif escolha == '7':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar_produto():
    print("\n=== Cadastro de  Produto ===")
    nome = input("Nome do produto: ")
    preco = float(input("Preço (R$): "))
    ingredientes = input("Ingredientes: ")

    produto = Produto(nome, preco, ingredientes)
    produtos.append(produto)
    print('Produto {nome} cadastrado com sucesso!'.format(nome=nome))


def cadastrar_cliente():
    print("\n=== Cadastro de  Cliente ===")
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cliente = Cliente(nome, telefone, email)
    clientes.append(cliente)
    print('Cliente {nome} cadastrado com sucesso!'.format(nome=nome))


def fazer_pedido():
    print("\n=== Fazer pedido ===")
    if not clientes:
        print("Nenhum cliente foi cadastrado.")
        return
    if not produtos:
        print("Nenhum produto foi cadastrado.")
        return
    print('clientes cadastrados')
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}.{cliente.nome}")
        try:
            indice_cliente = int(input("Escolha o número do cliente: ")) - 1
            cliente_escolhido = clientes[indice_cliente]
        except (IndexError, ValueError):
            print("Cliente inválido.")
            return
        produtos_escolhidos = []

        while True:
            print("\nProdutos disponíveis:")
            for i, produto in enumerate(produtos):
                print(f"{i + 1}. {produto.nome} - R${produto.preco:.2f}")

            escolha = input("Digite o número do produto (ou 'fim' para encerrar): ")

            if escolha.lower() == 'fim':
                break
            try:
                indice_produto = int(escolha) - 1
                produto_escolhido = produtos[indice_produto]
                produtos_escolhidos.append(produto_escolhido)
                print(f"Produto '{produto_escolhido.nome}' adicionado.")
            except (IndexError, ValueError):
                print("Produto inválido.")

        if not produtos_escolhidos:
            print("Nenhum produto foi selecionado. Pedido cancelado.")
            return

        novo_pedido = Pedido(cliente_escolhido, produtos_escolhidos)
        pedidos.append(novo_pedido)
        print(f"Pedido realizado com sucesso! Total: R${novo_pedido.total:.2f}")

def listar_produtos():
 if not produtos:
     print("Nenhum produto foi cadastrado.")
     return
 for produto in produtos:
     print(produto)
def listar_clientes():
         if not clientes:
            print("Nenhum cliente foi cadastrado.")
             for cliente in clientes:
                 print(cliente)
def listar_pedidos():
         if not pedidos:
             print("Nenhum pedido foi cadastrado.")
             for pedido in pedidos:
                 print(pedido)



menu()
