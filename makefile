all:
	python setup.py sdist

install:
	pip install .

test:
	python foo.py

publish:
	twine upload dist/* 

test-publish:
	twine upload --repository testpypi dist/*

set-up-venv:
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

# test.pypi doesn't have a supported version of argparse
install-from-test-pypi:
	pip install -i https://test.pypi.org/simple/ xl2thrift --extra-index-url https://pypi.org/simple argparse==1.4.0
