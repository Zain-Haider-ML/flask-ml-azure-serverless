install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C,no-member --max-line-length=120 train.py app.py
format:
	black --line-length 120 train.py app.py
	isort train.py app.py