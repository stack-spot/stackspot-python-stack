## Local development

In order to run locally the APIs you can execute ```make run```. This command lies in Makefile.
The script will make the api available on ```localhost:8080```.

## Folder Structure

```
<project_name>
	|__src
		|__<api domain>
		    |__ __init__.py
		    |__controller.py
		    |__usecase.py
        |__ __init__.py
	|__tests
		|__test_<api>_controller.py
    |__pyproject.toml
    |__Makefile
    |__README.md
```
