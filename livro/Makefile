all: serve

build:
	mkdocs build

clean:
	rm -rf html
	find . -type d -name "__pycache__" | xargs rm -rf {};

install:
	pip3 install --upgrade pip
	pip3 install mkdocs

requirements:
	pip3 install --upgrade setuptools
	pip3 install -r requirements.txt

serve:
	mkdocs serve
