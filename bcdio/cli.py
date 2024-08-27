import rich_click as click
from rich.console import Console

from .globals import sistema

console = Console()

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
def main():
    """Sistema bancário DIO CLI
    ## Comandos
    - Utilize os comandos abaixo:
    - Para depositar utilize o comando depositar e acrescente o valor exemplo ->> bcdio depositar 1000
    - Para sacar utilize o comando sacar e acrescente o valor exemplo ->> bcdio sacar 1000
    - Para mostrar o extrato utilize o comando ->> bcdio extrato
    - Para sair do sistema utilize o comando ->> bcdio sair
    """
    pass


@main.command()
@click.argument("valor", type=float)
def depositar(valor):
    """Depositar um valor na conta"""
    result = sistema.depositar(valor)
    console.print(result, style="green")


@main.command()
@click.argument("valor", type=float)
def sacar(valor):
    """Sacar um valor da conta"""
    result = sistema.sacar(valor)
    console.print(result, style="red")


@main.command()
def extrato():
    """Mostrar o extrato da conta"""
    extrato_text = sistema.mostrar_extrato()
    console.print(extrato_text, style="yellow")


@main.command()
def sair():
    """Sair do sistema"""
    console.print("Saindo do sistema...", style="yellow")


if __name__ == "__main__":
    main()
