from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def destampar(self):
        pass

    def escrever(self, texto):
        if self.destampar():
            print(f"[{self.cor.lower()}]{texto}[/]")


caneta = Caneta("Azul")
caneta.destampar()
caneta.escrever("OIIIII")

