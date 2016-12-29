init:
    pip install -r requirements.txt

test:
    python -m unittest discover
    
dist:
	python setup.py sdist

.PHONY: init test