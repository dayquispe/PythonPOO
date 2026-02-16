from concurrent.interpreters import list_all

from rich import print
from rich.panel import Panel

class Gamer:
    lista_jogos = []
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick


    def add_jogos_favoritos(self, nome_jogo):
        self.lista_jogos.append(nome_jogo)

    def ficha(self):
        texto = (f"Nome real: [black]{self.nome}[/]\n"
                 f"Jogos favoritos: \n")
        for i in self.lista_jogos:
            texto = f"\n:tomato:{i}"



        caixa = Panel(texto, title=f"Jogador: <{self.nick}>")
        print(caixa)

jogador = Gamer("Lucas", "Lukinha")
jogador.add_jogos_favoritos("Caçadores")
jogador.add_jogos_favoritos("ahhh")
jogador.ficha()
