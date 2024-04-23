all:
	python setup.py sdist

install:
	pip install .

test:
	python foo.py

publish:
	twine upload dist/* 

