from rich import print
from rich.panel import Panel

caixa = Panel("Esse daqui é só um panel de exemplo")
print(caixa)

caixa2 = Panel("[white]Esse daqui é só um painel de exemplo[/]", title="Mensagem", style="red")
print(caixa2)

caixa3 = Panel("[white]Esse daqui é só um painel de exemplo[/]", title="Mensagem", style="red", width=45, )
print(caixa3)