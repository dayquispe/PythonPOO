# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoas que temm nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome = "", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de intância
    def aniversario(self):
        self.idade +=1

    def __str__(self): # Dunder Method
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
# Declaração de Objeto
g1 = Gafanhoto("Maria", 20)
g1.aniversario()
# print(g1)

print(g1.__dict__) # Dunder Attribute
print(g1.__getstate__()) # Dunder Method
print(g1.__class__) # Dunder Attribute
print(g1.__doc__) #
print(g1)# Dunder Attribute