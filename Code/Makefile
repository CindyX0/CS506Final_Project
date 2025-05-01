# Makefile for setting up the Python project

setup:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run:
	. venv/bin/activate && jupyter notebook finalizedproject.ipynb

freeze:
	. venv/bin/activate && pip freeze > requirements.txt
