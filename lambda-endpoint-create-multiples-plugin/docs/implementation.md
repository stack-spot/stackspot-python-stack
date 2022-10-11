## **Implementation**

- **Step 1:** Apply plugin to create an endpoint:
	 
	```
	stk apply plugin lambda-endpoint-create-mulitples
	```

- **Step 2:** Type value for inputs:
	
	- **`resource_name`**: The name of the endpoint

	Example:
	```yaml
	- resource_name: Product
	```

    The following endpoints will be created:

    - [**`GET`**] product/get_all

    - [**`GET`**] product/get_by_id

    - [**`POST`**] product/create

    - [**`PUT`**] product/update

    - [**`DELETE`**] product/delete

- **Step 3:** Run your application locally:
	```
	stk run project
	```
	After that your application will be running on **`http://localhost:8080`**.

- **Step 4 (Optional):** Run the tests of your application:
	```
	stk run test
	```

- **Step 5 (Optional):** Run linter on your application to analyze and correct code formating:
	```
	stk run lint
	```

## **Project structure**

```
<project_name>
	|__src
		|__<resource>
			|__<operation_id>
				|__ __init__.py
				|__controller.py
				|__models.py
				|__usecase.py
        	|__ __init__.py
        |__ __init__.py
	|__tests
		|__integrations
			|__<resource>
				|__test_<resource>_<operation_id>_controller.py
	|__local.py
	|__poetry.toml
    |__pyproject.toml
	|__serverless.yaml
	|__README.md
```
