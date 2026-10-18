
from rich.console import Console

console = Console()

niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return "red"
    elif nivel == 2:
        return "yellow"
    elif nivel == 3:
        return "green"
    elif nivel == 4:
        return "cyan"
    elif nivel == 5:
        return "blue"
    else:
        return "white"

for i, mensagem in enumerate(niveis, start=1):
    cor = definir_cor(i)
    console.print(mensagem, style=cor, markup=False)
