# **Implementação**
Para implementar o Plugin é necessário saber os inputs, a estrutura da pasta e o local de desenvolvimento:

## **Inputs**

- **`command_name`**: A base do comando.
- **`command_description`**: Descrição que aparece quando utilizar o comando **`-help`**. 
- **`subcommand_description`**: Descrição do subcomando que aparece quando utilizar o comando **`-help`**.

## **Local development**
É recomendável utilizar um ambiente virtual para desenvolver sua CLI. 

Siga os passos abaixo para usar o ambiente virtual de Python:

**Passo 1.** Gere o ambiente usando o comando:

```
make create-env
``` 
**Passo 2.** Ative o ambiente chamando o script **`activate`** na **`env/bin`**, veja o exemplo abaixo:
```
source env/bin/activate
``` 

**Passo 3.** Adicione o **`cli.py|main`** como ponto de entrada, com isso ocorre a ativação do ambiente virtual virtual.

**Passo 4.** Instale as dependencias no seu ambiente virtual com o comando:
```
make install
```  
**Passo 5.** Envie os comandos para o seu CLI usando:
```
cli_command_name
``` 
**Passo 6.** Agora execute: 
```
<cli_command_name> <command> <subcommand> Stacker!
``` 

## **Estrutura da pasta**

```
<nome_projeto>
	|__<nome_projeto>
			|__cli.py
			|__ __init__.py
			|__comandos
				|__ __init__.py
                |__<comando>
                	|__<subcomando>.py
	|__tests
		|__test_<comando>_<subcomando>.py
	|__pyproject.toml
|__Makefile
```