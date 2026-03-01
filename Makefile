all: format lint test

format:
	ruff format .

lint:
	ruff check .

test:
	pytest
