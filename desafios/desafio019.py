from rich import print
from time import sleep
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você está na [yellow]página {self.pagina_atual}[/][/]")

    def avancar_paginas(self, quantidade_de_paginas):
        for i in range(self.pagina_atual, self.pagina_atual + quantidade_de_paginas):
            if self.pagina_atual < self.paginas:
                print(f"Pág{i+1}:arrow_forward:", end=" ")
                sleep(1)
                self.pagina_atual+=1
            else:
                print(f":closed_book:[red]Você chegou ao final do livro'{self.titulo}'[/]")
                break
        print(f"[blue]Você avançou {quantidade_de_paginas} páginas e agora está na [yellow]página {self.pagina_atual}[/]")


livro = Livro("Livro Day", 20)
livro.avancar_paginas(8)
livro.avancar_paginas(8)
livro.avancar_paginas(10)


