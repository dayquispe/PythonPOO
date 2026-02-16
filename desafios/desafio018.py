from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, nome_churrasco, quantidade_pessoas):
        self.nome_churrasco = nome_churrasco
        self.quantidade_pessoas = quantidade_pessoas


    def peso_total(self):
        consumo_padrao = 0.400
        return consumo_padrao * self.quantidade_pessoas

    def preco_total(self):
        preco_kg = 82.40
        return self.peso_total() * preco_kg

    def valor_por_pessoa(self):
        return self.preco_total() / self.quantidade_pessoas

    def analisar(self):
        texto = (f"Analisando [green]{self.nome_churrasco}[/] com [blue]{self.quantidade_pessoas} convidados[/]\n"
                 f"Cada participante comera 0.4Kg e cada Kg custa R$82.40\n"
                 f"Recomendo [blue]comprar {self.peso_total():.2f}Kg[/] de carne\n"
                 f"O custo total será de [green]R${self.preco_total():.2f}[/]\n"
                 f"Cada pessoa pagará [yellow]R${self.valor_por_pessoa():.2f}[/] para participar.")
        return print(Panel(texto, title=self.nome_churrasco))


# Considerar:
#Consumo padrão: 400g por pessoa
#Preço: R$82,40/Kg

churrasco = Churrasco("Churrasco dos amigos",  15)
churrasco.analisar()