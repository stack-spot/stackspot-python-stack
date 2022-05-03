from click.testing import CliRunner
from {{project_name_sanitized}}.cli import cli

def test_say_hello():
    runner = CliRunner()
    result = runner.invoke(cli, ["{{inputs.command}}", "{{inputs.subcommand}}", "stacker"])
    
    assert result.exit_code == 0
    assert result.output == "Subcommand {{inputs.subcommand}} with argument value stacker!\n"