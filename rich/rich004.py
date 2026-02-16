print(int.__doc__)
print("______________________________________________________")
print(int.__dict__)
print("______________________________________________________")
from rich import print
print(int.__dict__)

print("______________________________________________________")
from rich import inspect
inspect(int, all=True)

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0): # Aqui dentro dos parenteses temos os nomes dos parâmetros.
        # aqui abaixo temos os parametros
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
        else:
            print(f"Saque NEGADO ! \n"
                  f"Saldo insuficiente para o saque no valor de R${valor:,.2f}")

c = ContaBancaria(111, "José Antônio", 450)
inspect(c)
