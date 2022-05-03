Develop and create your own CLI using Python and Click (https://click.palletsprojects.com/en/8.1.x/)

Our stack has the basic template for creating a python project using poetry(https://python-poetry.org/) and pytest(https://docs.pytest.org/en/7.1.x/). With this template you can create a basic python project to develop your projects or use this template together with our plugins to create your custom CLI.

With the available plugins in this stack, you will be able to develop a custom CLI using the click framework and add new commands to your CLI.

The Python CLI Stack was developed using the best practices in software architecture:

- Test driven development.
- Clean Architecture.
- Decoupled components.
- New commands can be added in a blink of a eye.



Template python-app-template

```
<project_name>
	|__<project_name>
			|__ __init__.py
	|__tests
	|__pyproject.toml
|__Makefile
```

Plugin CLI

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

Plugin add command

```
<project_name>
	|__<project_name>
			|__cli.py
			|__ __init__.py
			|__commands
				|__ __init__.py
                |__<verb>
                	|__<domain>.py
	|__tests
		|__test_<verb>_<domain>.py
	|__pyproject.toml
|__Makefile
```

