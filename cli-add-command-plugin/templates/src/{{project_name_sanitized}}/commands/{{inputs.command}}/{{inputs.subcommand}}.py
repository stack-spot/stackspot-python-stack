import click

@click.command()
@click.argument("{{inputs.argument}}")
@click.pass_context
def {{inputs.subcommand}}(ctx, {{inputs.argument}}: str):
    """{{inputs.subcommand_description}}"""
    print("Subcommand {} with argument value {}!".format("{{inputs.subcommand}}", {{inputs.argument}}))
