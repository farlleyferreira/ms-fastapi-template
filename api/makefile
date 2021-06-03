coverage:
	python -m pytest -v --cov-report term-missing --cov=project/ --cov-report=xml

test:
	python -m pytest

list-requirements:
	pip freeze

lint:
	python -m black project\

install-requirements:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

run-aplication:
	python setup.py

sonar-scan:
	../ops/sonar-scanner-4.6.0.2311-windows/bin/sonar-scanner.bat 

radon-scan:
	radon cc project/ -a