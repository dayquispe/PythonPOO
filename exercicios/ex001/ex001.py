# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de instância
        self.nome = ""
        self.idade= 0

    # Métodos de intância
    def aniversario(self):
        self.idade +=1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Objeto

g1 = Gafanhoto()
g1.nome = "Dayana"
g1.idade = 20
g1.aniversario()
print(g1.mensagem())