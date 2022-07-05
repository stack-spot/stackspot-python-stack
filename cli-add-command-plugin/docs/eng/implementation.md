# **Implementation**
To implement the Python Stack is necessary know the inputs, local development and the folder structure.  

## **Inputs**

- **`command_name`**: The base command name.
- **`command_description`**: Description for the command that will appear when you use **`-help`** command.
- **`subcommand_description`**: Description for the subcommand taht will appear when you use the **`-help`** command.

## **Local development**

We recommend the use of a virtual environment to develop your CLI. Follow these steps to use the Python virtual environment.
**Step 1.** Generate the environment using the included command:
```
make create-env
``` 
**Step 2.** Activate your environment by calling the Script **`activate`** on **`env/bin`**, see the example below:
```
source env/bin/activate
``` 
**Step 3.** Add the **`cli.py|main`** as entry point to activate a virtual environment.

**Step 4.** Install the dependencies in your virtual environment with:
```
make install
```  
**Step 5.** Send the commands to your CLI using:
```
cli_command_name
``` 

**Step 6.** Now, execute: 
```
<cli_command_name> <command> <subcommand> Stacker!
``` 
## **Folder Structure**

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