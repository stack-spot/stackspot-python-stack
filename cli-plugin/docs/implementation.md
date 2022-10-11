## **Implementation**

- **Step 1:** Create your CLI 
	```
	stk apply plugin cli-plugin
	```

- **Step 2:** Type value for input
	- **`CLI Command Name`**: Type the name of your CLI
	
	Example: 
	```
	command_name: my-own-cli
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

- **Step 4:** Execute your newer command line interface:	
	```
	<cli_command_name> <command> <subcommand> <your-desidered-text>!
	``` 

	Example:
	```
	my-own-cli say hello Stacker!
	```

## **Project structure**

```
<project_name>
	|__<src>
		<project_name>
			|__ commands
				|__ say
					|__ __init__.py
					|__ hello.py
				|__ __init__.py
			|__ cli.py
			|__ __init__.py
		|__ tests
			|__ __init__.py
			|__ test_say_hello.py
	|__ pyproject.toml
	|__ stk.yml
```
