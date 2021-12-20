POETRY=poetry
PYTEST=$(POETRY) run pytest --cache-clear --cov-config=.coveragerc --cov=app tests/ --cov-report=xml > pytest-coverage.txt
MYPY=$(POETRY) run mypy --ignore-missing-imports
BLACK=$(POETRY) run black
ISORT=$(POETRY) run isort
PYLINT=$(POETRY) run pylint
UVICORN=$(POETRY) run uvicorn
PACKAGE=app

install:
	$(POETRY) install
	$(POETRY_EXPORT)

update:
	$(POETRY) update
	$(POETRY_EXPORT)

test:
	$(PYTEST) -vv

fmt:
	$(ISORT) main.py ./${PACKAGE} ./tests
	$(BLACK) main.py ./${PACKAGE} ./tests

lint:
	$(MYPY) main.py ./${PACKAGE}/
	$(PYLINT) main.py ./${PACKAGE}

build:
	$ docker-compose build

run: build
	$ docker-compose up

testBDD:
	behave ./tests/features

all: fmt lint test build run
