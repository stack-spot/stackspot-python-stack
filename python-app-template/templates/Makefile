## Setup
install:
	cd src; pip install .

# Test
test:
	cd src; pytest -v tests/

# Execute
run:
	python src/{{project_name_sanitized}}/__init__.py 

# Activate env
activate:
	python3 -m venv env; make install