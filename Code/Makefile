
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
NOTEBOOK = finalizedproject.ipynb

# Create virtual environment and install dependencies
setup:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run Jupyter Notebook
run:
	$(PYTHON) -m notebook $(NOTEBOOK)

# Freeze current dependencies into requirements.txt
freeze:
	$(PIP) freeze > requirements.txt

# Remove the virtual environment
clean:
	rm -rf $(VENV_DIR)
