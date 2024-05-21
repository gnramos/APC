all: serve

build:
	mkdocs build

install: requirements
	pip3 install --upgrade setuptools
	pip3 install -r requirements.txt

serve:
	mkdocs serve
