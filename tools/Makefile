# Makefile for Python developement

# replace <source_package> with your application's package name
PACKAGE=<source_package>

NPROC := $(shell nproc)
PYTHONFILES := $(shell find . -name '*.py')

all: lint coverage

# repository cleanup
clean:
	@rm -rf build dist
	@find . -name "*.pyc" -delete

distclean:
	@git clean -xdf

# syntax checking
lint: isort pep8 pep257 pylint

isort: clean
	@echo "=== isort ==="
	@isort $(PYTHONFILES) --check-only || true

pep%: clean
	@echo "=== PEP$* ==="
	@pep$* $(PYTHONFILES) || true

pylint: clean
	@echo "=== Pylint ==="
	@pylint -j $(NPROC) $(PYTHONFILES) || true

# unitary tests, code coverage
basic_coverage: clean
	@echo "=== Coverage ==="
	@coverage run --source=$(PACKAGE) -m unittest discover -s tests
	@coverage report

coverage: clean basic_coverage
	@rm -rf htmlcov
	@coverage html

test: clean
	@python -m unittest discover -s tests
