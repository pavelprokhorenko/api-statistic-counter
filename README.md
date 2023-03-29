# Statistic counter microservice

## Dependencies

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* Third-part python packages from `backend/requirements.txt`.

## Config

* Create ".env" file and add environment variables to it:
```dotenv
# base
TITLE="Statistic Manager"
VERSION="0.1.0"
DEBUG=True

# server
BACKEND_SERVER_HOST=0.0.0.0
BACKEND_SERVER_PORT=8000
BACKEND_SERVER_WORKERS=1

ALLOWED_ORIGINS=["https://localhost","http://localhost","https://localhost:3000","http://localhost:3000"]
ALLOWED_METHODS=["*"]
ALLOWED_HEADERS=["*"]

# postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=postgres

IS_POSTGRES_ECHO_LOG=false
IS_POSTGRES_SESSION_EXPIRE_ON_COMMIT=false
```

* Other project settings you can find in "app/core/config.py"

## Migrations

* After creating the model in `backend/src/models`, you need to import it in `backend/src/db/base.py` (in order to make it visible to alembic)
* Make migration

```console
$ alembic revision --autogenerate -m "add column last_name to User model"
```

* Run migrations

```console
$ alembic upgrade head
```

* Postgres
```console
$ alembic revision --autogenerate -m "text"
$ alembic upgrade head
$ alembic downgrade -1
```

## API Docs

* All information about REST API endpoints you can find in Swagger docs (default - http://127.0.0.1:8000/docs)
