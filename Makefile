.PHONY: test
test:
	python setup.py install
	nosetests -s
