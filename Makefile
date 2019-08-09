init:
		pip install pipenv --upgrade
		pipenv install --dev
		pipenv install -e .

test: install-local
		pipenv run test

install-local:
		python3 setup.py sdist bdist_wheel
		pip3 install -e .