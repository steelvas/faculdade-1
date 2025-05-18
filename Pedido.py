class Pedido:
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos
        self.total = sum(produto.preco for produto in produtos)

    def __str__(self):
        nomes_produtos = ', '.join([p.nome for p in self.produtos])
        return f"Cliente: {self.cliente.nome} | Produtos: {nomes_produtos} | Total: R${self.total:.2f}"