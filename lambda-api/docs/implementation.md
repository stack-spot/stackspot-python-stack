## **Local development**

Para executar suas APIs localmente, execute:
```
make run
``` 
Esse comando está no **`makefile`**. 

- Depois disso o script mostra a API disponível no **```localhost:8080```**.

## **Estrutura da pasta**

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
