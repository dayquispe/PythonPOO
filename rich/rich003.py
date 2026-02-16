from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")
tabela.add_column("Nome", justify="center", style="blue")
tabela.add_column("Preço", justify="center", style="white")
tabela.add_row("Camisa", "R$78,00")
tabela.add_row("Bermuda", "R$150,00")
print(tabela)