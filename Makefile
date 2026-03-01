all: format lint test

format:
	ruff format .

lint:
	ruff check .

test:
	python -m pytest app/tests/test_items.py
