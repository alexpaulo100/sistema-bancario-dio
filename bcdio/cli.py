import rich_click as click
from rich.console import Console
from rich.table import Table

from .core import SistemaBancario

console = Console()
sistema = SistemaBancario()


click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option("0.1.1")
def main():
    """Sistema bancário DIO CLI
    ## Comandos
    - Utilize os comandos abaixo:
    - Para criar um novo usuário use o comando ->> bcdio criar-usuario
    - Para criar uma nova conta use o comando ->> bcdio criar-conta
    - Para ver seu relatório de contas use o comando ->> bcdio listar-contas
    - Para depositar utilize o comando depositar e acrescente o valor exemplo
    ->> bcdio depositar 1000
    - Para sacar utilize o comando sacar e acrescente o valor exemplo ->> bcdio sacar 1000
    - Para mostrar o extrato utilize o comando ->> bcdio extrato
    - Para excluir um usuário utilize o comando ->> bcdio excluir-usuario
    - Para excluir uma conta utilize o comando ->> bcdio excluir-conta
    - Para sair do sistema utilize o comando ->> bcdio sair
    """
    pass


@main.command()
def depositar():
    """Comando para depositar um valor em uma conta"""
    # Solicitar o valor do depósito
    valor = click.prompt("Informe o valor do depósito", type=float)
    # Solicitar o CPF do usuário
    cpf = click.prompt("Informe o CPF do usuário (somente números)", type=str)
    # Solicitar o número da conta
    numero_conta = click.prompt("Informe o número da conta", type=int)

    try:
        sistema.depositar(cpf, numero_conta, valor)
        click.echo(
            click.style(
                f"Depósito de R$ {valor:.2f} realizado com sucesso na conta número {numero_conta}.",
                fg="green",
            )
        )
    except ValueError as e:
        click.echo(f"Erro: {e}")


@main.command()
def sacar():
    """Sacar um valor da conta"""
    cpf = click.prompt("Informe o CPF do usuário (somente números)", type=str)
    numero_conta = click.prompt("Informe o número da conta", type=int)
    valor = click.prompt("Informe o valor do saque", type=float)
    try:
        # Verifique se o usuário existe
        usuario_id = sistema._obter_usuario_id_por_cpf(cpf)
        if not usuario_id:
            raise ValueError("Usuário não encontrado.")

        # Realiza o saque
        sistema.sacar(cpf, numero_conta, valor)

        console.print("[bold green]Saque realizado com sucesso![/bold green]")
        console.print(f"Valor: R${valor:.2f}")
        console.print(f"Conta: {numero_conta}")

    except ValueError as e:
        console.print(f"[bold red]Erro:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]Erro:[/bold red] {e}")


@main.command()
def extrato():
    """Exibe o extrato da conta especificada pelo CPF e número da conta"""
    cpf = click.prompt("Informe o CPF do usuário (somente números)", type=str)
    numero_conta = click.prompt("Informe o número da conta", type=int)

    sistema = SistemaBancario()

    try:
        saldo, movimentacoes = sistema.obter_extrato(cpf, numero_conta)

        # Exibindo o saldo
        table = Table(title="Extrato")
        headers = ["Conta", "CPF", "Saldo"]
        for header in headers:
            table.add_column(header, style="magenta")

        table.add_row(str(numero_conta), cpf, f"R${saldo:.2f}")
        console.print(table)

        # Exibindo movimentações, se houver
        if movimentacoes:
            table = Table(title="Movimentações")
            headers = ["Tipo", "Valor", "Data"]
            for header in headers:
                table.add_column(header, style="yellow", width=20)

            for mov in movimentacoes:
                tipo = "Depósito" if mov.tipo == "deposito" else "Saque"
                data_formatada = mov.data.strftime("%Y-%m-%d %H:%M:%S")
                valor_formatado = f"R${mov.valor:.2f}"

                table.add_row(tipo, valor_formatado, data_formatada)

            console.print(table)
        else:
            console.print(
                f"[bold yellow]Não há movimentações para a"
                f"conta número{numero_conta}.[/bold yellow]"
            )

    except ValueError as e:
        console.print(f"[bold red]Erro:[/bold red] {e}")


# Adiciona o comando 'extrato' ao grupo principal
main.add_command(extrato)


@main.command()
def criar_usuario():
    """Criar um novo usuário"""
    nome = click.prompt("Informe seu nome completo")
    cpf = click.prompt("Informe seu CPF (somente números)")
    data_nascimento = click.prompt("Informe sua data de nascimento (dd-mm-aaaa)")

    endereco = {
        "logradouro": click.prompt("Informe seu logradouro"),
        "numero": click.prompt("Informe o número"),
        "bairro": click.prompt("Informe seu bairro"),
        "cidade": click.prompt("Informe a cidade"),
        "estado": click.prompt("Informe o estado (somente a sigla, exemplo: SP)"),
    }

    try:
        novo_usuario = sistema.criar_usuario(nome, cpf, data_nascimento, endereco)
        console.print(f"Usuário {novo_usuario.nome} criado com sucesso!", style="green")
    except ValueError as e:
        console.print(f"Erro ao criar usuário: {e}", style="red")


@main.command()
def excluir_usuario():
    """Excluir um usuário do sistema"""
    cpf = click.prompt("Informe o CPF do usuário (somente números)", type=str)

    try:
        resultado = sistema.excluir_usuario(cpf)
        if resultado:  # Verifica se o resultado não é None
            console.print(resultado, style="green")
    except ValueError as e:
        console.print(f"Erro ao excluir usuário: {e}", style="red")


@main.command()
def criar_conta():
    """Crie sua conta corrente"""
    cpf = click.prompt("Informe o CPF do usuário (somente números):", type=str)
    try:
        nova_conta = sistema.criar_conta(cpf)  # Passar o CPF como argumento
        console.print(
            f"Conta criada com sucesso! Número da conta: {nova_conta.numero}",
            style="green",
        )
    except ValueError as e:
        console.print(f"Erro ao criar conta: {e}", style="red")


@main.command()
def excluir_conta():
    """Exclui uma conta bancária"""
    cpf = click.prompt("Informe o CPF do usuário (somente números):", type=str)
    numero_conta = click.prompt("Informe o número da conta a ser excluída:", type=int)

    try:
        resultado = sistema.excluir_conta(cpf, numero_conta)
        click.echo(resultado)
    except ValueError as e:
        click.echo(f"Erro: {e}")
    except Exception as e:
        click.echo(f"Erro inesperado: {e}")


@main.command()
def listar_contas():
    """Relatório de suas contas"""
    cpf = click.prompt("Informe o CPF do usuário (somente números):", type=str)

    try:
        # Chama o método listar_contas e captura o retorno
        contas = sistema.listar_contas(cpf)

        if isinstance(contas, str):
            click.echo(contas)
            return

        table = Table(title="Contas do Usuário", caption="Relatório de Contas")
        table.add_column("Nome", style="cyan bold", no_wrap=True)
        table.add_column("Número", style="cyan bold", no_wrap=True)
        table.add_column("Agência", style="magenta")
        table.add_column("Saldo", style="green")

        for conta in contas:
            nome = conta.get("nome", "N/A")
            numero = conta.get("numero", "N/A")
            agencia = conta.get("agencia", "N/A")
            saldo = f"R$ {conta.get('saldo', 0.0):.2f}"
            table.add_row(nome, str(numero), agencia, saldo)

        console.print(table)

    except ValueError as e:
        click.echo(f"Erro: {e}")
    except Exception as e:
        click.echo(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
