## Setup
install:
	poetry config virtualenvs.create false
	cd src; poetry install

# Test
test:
	cd src; pytest -v tests/

# Execute
run:
	python src/{{project_name_sanitized}}/__init__.py 

# create env
create-env:
	python3 -m venv env