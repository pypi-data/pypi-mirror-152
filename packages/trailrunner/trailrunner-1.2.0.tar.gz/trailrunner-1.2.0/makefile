SRCS:=trailrunner

.venv:
	python -m venv .venv
	source .venv/bin/activate && make setup dev
	echo 'run `source .venv/bin/activate` to use virtualenv'

venv: .venv

dev:
	python -m pip install -e .

setup:
	python -m pip install -U pip
	python -m pip install -Ur requirements-dev.txt

release: lint test clean
	flit publish

format:
	python -m ufmt format $(SRCS)

lint:
	python -m mypy --strict $(SRCS)
	python -m flake8 $(SRCS)
	python -m ufmt check $(SRCS)

test:
	python -m coverage run -m $(SRCS).tests
	python -m coverage report
	python -m coverage html

.PHONY: html
html: .venv README.md docs/*.rst docs/conf.py
	source .venv/bin/activate && sphinx-build -ab html docs html

clean:
	rm -rf build dist README MANIFEST *.egg-info .mypy_cache html

distclean: clean
	rm -rf .venv
