# Implementation

#Inputs

- cli_command_name - The base command that will be used to invoke the CLI.

#Local development

We recommend the use of a virtual environment to develop your CLI. Follow these steps to use the Python virtual environment.
1 - You can generate this env using the included make command: `make create-env`.
2 - After creating your venv you can activate it by calling the Script `activate` on `env/bin`, like: `source env/bin/activate`.
3 - This will activate a virtual enviroment having the cli.py|main as entry point.
4 - Now you can install the dependencies in your venv with `make install`.
5 - You can now send commands to your cli using the `cli_command_name`.
6 - Try: `<cli_command_name> say hello Stacker!`

#Folder Structure

```
<project_name>
	|__<project_name>
			|__cli.py
			|__ __init__.py
			|__commands
				|__ __init__.py			
	|__tests
		|__test_cli.py
	|__pyproject.toml
|__Makefile
```