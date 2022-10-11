## **Implementation**

- **Step 1:** Create new command line to your existing STK CLI 
	```
	stk apply plugin cli-add-command-plugin
	```
	
- **Step 2:** Type value for inputs

	- **`command_name`**: The name of command

	- **`command_description`**: Description of the new command base that will show when use **`--help`** option.
	
	- **`subcommand_name`**: The name of sub command of command

	- **`subcommand_description`**: Description of the new subcommand of command that will show when use  **`--help`**.

	- **`argument_name`**: Descrição do subcomando que aparece quando utilizar o comando **`--help`**.

	Example:

	```yaml
	command_name: my_command
	command_description: My description for my_command
	subcommand_name: my_sub_command
	subcommand_description: My description for my_sub_command
	argument_name: name
	```

- **Step 3:** Active your environment calling the script according your S.O., execute the command below:
	- Windows: 
		```
		.venv\Scripts\activate
		```

	- Linux or Mac: 
		```
		source .venv/bin/activate
		```

- **Step 4:** Execute your newer command line:	
	```
	<cli_command_name> <command> <subcommand> <your-desidered-text>!
	``` 

	Example:
	```
	my-own-cli my-command my-sub-command 'Hello World'
	```

## **Project structure**

```
<project_name>
	|__ <src>
		|__ <project_name>
			|__ __commands
                |__ <command>
					|__ __init__.py
                	|__ <subcommand>.py
				|__ __init__.py
			|__ cli.py
			|__ __init__.py
		|__ tests
			|__ __init__.py
			|__ test_<command>_<subcommand>.py
	|__ pyproject.toml
	|__ stk.yml
```
