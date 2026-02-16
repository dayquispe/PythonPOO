from rich import print
from rich import inspect
class Funcionario:
    """
    Cria Funcionarios e permite ele se apresentar
    """
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        print(f" :smile: Olá sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}.")


c1 = Funcionario("Dayana", "TI", "Programador")
c1.apresentacao()

c2 = Funcionario("Thiago", "Administração", "Diretor")
c2.apresentacao()

inspect(c1)
inspect(Funcionario)
inspect(c1, dunder=True)