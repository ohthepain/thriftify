all:
	python setup.py sdist

install:
	pip install .

test:
	python foo.py

publish:
	twine upload dist/* 

# test.pypi doesn't have a supported version of argparse
install-from-test-pypi:
	pip install -i https://test.pypi.org/simple/ xl2thrift --extra-index-url https://pypi.org/simple argparse==1.4.0
