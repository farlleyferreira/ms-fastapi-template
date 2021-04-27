coverage:
	python -m pytest -v --cov-report term-missing --cov=project/ --cov-report=xml

test:
	python -m pytest

list-requirements:
	pip freeze

install-requirements:
	pip install -r requirements.txt

run-aplication:
	python setup.py

sonar-scan:
	../../ops/sonar-scanner-4.6.0.2311-windows/bin/sonar-scanner.bat 

