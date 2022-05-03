import click

from {{project_name_sanitized}}.commands.{{inputs.command}}.{{inputs.subcommand}} import {{inputs.subcommand}}

@click.group()
def {{inputs.command}}():
    """{{inputs.command_description}}"""
    pass

{{inputs.command}}.add_command({{inputs.subcommand}})