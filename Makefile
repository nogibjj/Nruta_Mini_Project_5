install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_*?py *.py

test:
	python -m pytest -cov=main test_*.py

all: install format lint test