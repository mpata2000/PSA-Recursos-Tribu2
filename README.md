# PSA Recursos - Tribu 2 - Suqad 11
[![codecov](https://codecov.io/gh/mpata2000/PSA-Recursos-Tribu2/branch/main/graph/badge.svg?token=T726IGKKWO)](https://codecov.io/gh/mpata2000/PSA-Recursos-Tribu2) [![Tests](https://github.com/mpata2000/PSA-Recursos-Tribu2/actions/workflows/test.yml/badge.svg)](https://github.com/mpata2000/PSA-Recursos-Tribu2/actions/workflows/test.yml) [![Linters](https://github.com/mpata2000/PSA-Recursos-Tribu2/actions/workflows/linters.yml/badge.svg)](https://github.com/mpata2000/PSA-Recursos-Tribu2/actions/workflows/linters.yml) [![Deploy](https://github.com/mpata2000/PSA-Recursos-Tribu2/actions/workflows/deploy.yml/badge.svg)](https://github.com/mpata2000/PSA-Recursos-Tribu2/actions/workflows/deploy.yml)


## Technologies

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Poetry](https://python-poetry.org/)
* [Docker](https://www.docker.com/)
* [Heroku](https://www.heroku.com/)

## Deployed DOCS

https://psa-tribu2-recursos.herokuapp.com/docs

## Architecture

Directory structure (based on [Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/)):

```tree
├── main.py
├── app
│   ├── domain
│   │   ├── hours
│   │   │   ├── hours.py  # Entity
│   │   │   ├── hours_exception.py  # Exception definitions
│   │   │   └── hours_repository.py  # Repository interface
│   │   └── resources
│   │       ├── resources.py  # Entity
│   │       └── resources_exception.py  # Exception definitions
│   ├── infrastructure
│   │    ├── hours
│   │    │   ├── hours_dto.py  # DTO using SQLAlchemy
│   │    │   ├── hours_query_service.py  # Query service implementation
│   │    │   └── hours_repository.py  # Repository implementation
│   │    └── database.py
│   ├── presentation
│   │   └── schema
│   │       ├── hours
│   │       │   └── hours_error_message.py
│   │       └── resources
│   │           └── resources_error_message.py
│   └── usecase
│       ├── hours
│       │   ├── hours_command_model.py  # Write models including schemas of the RESTFul API
│       │   ├── hours_command_usecase.py
│       │   ├── hours_query_model.py  # Read models including schemas
│       │   ├── hours_query_service.py  # Query service interface
│       │   └── hours_query_usecase.py
│       └── resources
│           └── resources_query_model.py  # Read models including schemas
└── tests
```

## Run
``` bash
make run
```

Access api swagger at: http://127.0.0.1:8000/docs#/

## Tests
``` bash
make test
```

## Reformat

``` bash
make fmt
```

## Lint

``` bash
make lint
```

## Test BDD

Make sure the api is running

``` bash
make run
```

and run the test with

``` bash
make testBDD
```
