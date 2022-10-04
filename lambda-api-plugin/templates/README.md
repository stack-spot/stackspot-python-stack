Python Plugin for API Lambdas
==============================

This project presents a template to develop API Lambdas in Python using:

- [FastAPI](https://fastapi.tiangolo.com/) web framework to create APIs
- [Serverless](https://www.serverless.com/framework) framework to help deploy lambdas in AWS

The reasons that led to the choice of these frameworks can be found in [ADR002]().

## Install dependencies

To install poetry and npm dependencies execute: ```make install```.

## Run Locally

To run APIs locally execute: ```make run```.
The script will make the api available on ```localhost:8080```.

## Automatic docs

FastAPI gives Interactive API documentation and exploration web user interfaces. As the framework is based on OpenAPI, there are multiple options, 2 included by default.
- **Swagger** UI, with interactive exploration, call and test your API directly from the browser. You can access with path ``` /docs```
- Alternative API documentation with **ReDoc**.  You can access with path ``` /redoc```

## Run Tests

To run tests execute: ```make test```. This will run all tests in the folder ```tests```.

## Lint and Auto-formatter

**Lint** is a static code analysis tool used to flag programming errors, bugs, stylistic errors.

To auto-formatter and execute validations: ```make lint```

To change the validation rules, just edit the `.flake8` file. For more details
see: https://flake8.pycqa.org/en/latest/user/violations.html

## Deploy

To deploy it is necessary that the aws credentials are set in .aws folder in ```config``` and ``` credentials```  files. After that just run ```make deploy```.
