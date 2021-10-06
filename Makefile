install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app

test:
	pytest -vv --cov-report term-missing --cov=mylib test_*.py

format:
	black *.py