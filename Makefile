test:
	pipenv run pytest

lint:
	pipenv run black .

solve:
	pipenv run python advent2020.py $(day)
