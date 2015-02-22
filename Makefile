.PHONY: test
test:
	python setup.py install
	nosetests -s

.PHONY: clean
clean:
	rm -rf build dist slask.egg-info
