class Produto:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} | Ingredientes: {self.ingredientes}"

