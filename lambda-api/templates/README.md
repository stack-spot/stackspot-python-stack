## Testar local

1. Install dependencies
On the `root` folder, run:
``
make install
``

2. subir local
On the `root` folder, run:
``
python3 local.py
``

## Subir na AWD

1. install poetry
   ``
   export PATH=$PATH:$HOME/.poetry/bin
   ``

2. creates a virtual environment
   ``
   poetry env use 3.8
   ``

3. install dependencies
   ``
   poetry install
   ``

4. install plugin serverless-python-requirements (the plugin will bundle your python dependencies specified in your
   requirements.txt when you run sls deploy)
   ``
   npm install
   ``

5. create requirements file for deploy
   ``
   poetry export -f requirements.txt -o requirements.txt
   ``

6. configure your credentials and config aws files in .aws for deploy

7. deploy
   ``
   sls deploy
   ``

8. to deactivate virtual environment
   ``
   deactivate
   ``

## Lint

**Lint** is a static code analysis tool used to flag programming errors, bugs, stylistic errors.

To execute validations: ``` poetry run flake8 src/ tests/```

To change the validation rules, just edit the `.flake8` file. For more details
see: https://flake8.pycqa.org/en/latest/user/violations.html

## Auto-formatter

Automatic formats the code following the PEP8 rules and respecting the config in `.flake8` file.

To format all code: ```poetry run autopep8 --in-place --recursive --aggressive --aggressive src/ tests/```
