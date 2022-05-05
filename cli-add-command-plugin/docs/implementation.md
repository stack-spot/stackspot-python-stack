#Inputs

- command_name - The base command name.
- command_description - Description for the command that will appear on the helper.
- subcommand_description - Description for the subcommand taht will apperar on the helper.

#Local development

We recommend the use of a virtual environment to develop your CLI. Follow these steps to use the Python virtual environment.
1 - You can generate this env using the included make command: `make create-env`.
2 - After creating your venv you can activate it by calling the Script `activate` on `env/bin`, like: `source env/bin/activate`.
3 - This will activate a virtual enviroment having the cli.py|main as entry point.
4 - Now you can install the dependencies in your venv with `make install`.
5 - You can now send commands to your cli using the `cli_command_name`.
6 - Try: `<cli_command_name> <command> <subcommand> Stacker!`

#Folder Structure

```
<project_name>
	|__<project_name>
			|__cli.py
			|__ __init__.py
			|__commands
				|__ __init__.py
                |__<command>
                	|__<subcommand>.py
	|__tests
		|__test_<command>_<subcommand>.py
	|__pyproject.toml
|__Makefile
```