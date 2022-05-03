import click

from {{project_name_sanitized}}.commands.say.hello import hello

@click.group()
def say():
    """Command to say a text."""
    pass

say.add_command(hello)