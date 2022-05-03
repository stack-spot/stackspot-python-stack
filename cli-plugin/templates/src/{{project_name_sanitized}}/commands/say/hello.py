import click

@click.command()
@click.argument("name")
@click.pass_context
def hello(ctx, name: str):
    """Command to say hello"""
    print(f"Hello {name}!")
