
from rich.console import Console

console = Console()

def definir_cor(nivel):
    if nivel <= 20:
        return "red", "Muito baixo (crítico)"
    elif nivel <= 40:
        return "yellow", "Baixo"
    elif nivel <= 60:
        return "green", "Médio"
    elif nivel <= 80:
        return "cyan", "Alto"
    elif nivel <= 100:
        return "blue", "Muito alto (alerta)"
    else:
        return "white", "Valor inválido"

nivel_agua = 15

if 0 <= nivel_agua <= 100:
    cor, situacao = definir_cor(nivel_agua)
    console.print(
        f"Nível da água: {nivel_agua}%",
        style=cor
    )
    console.print(f"Situação: {situacao}", style=cor)
else:
    console.print("Porcentagem inválida!", style="bold red")

