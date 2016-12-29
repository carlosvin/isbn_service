init:
    pip install -r requirements.txt

test:
    py.test tests
    
dist:
	python setup.py sdist

.PHONY: init test