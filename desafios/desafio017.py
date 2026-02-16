from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto = f"{" " * 14}{self.nome}\n{"-" * 35}\n{"." * 13}R${self.preco:,.2f}{"." * 12}"
        return print(Panel(texto, title="Produto", width=40))

p = Produto("Celular", 4_000.00)

p.etiqueta()