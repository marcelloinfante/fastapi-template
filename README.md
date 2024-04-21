![_0d9dff30-31b7-499c-ae59-2787aa630094](https://github.com/marcelloinfante/happy-scribe-api/assets/80683232/31e06e26-d3f6-4295-9370-9040ad329222)

# Happy Scribe API

## Quick Start

1. Install [Docker](https://www.docker.com) on your machine.
2. Start Docker.
3. Add the environment variables in the .env file.
4. Open the terminal in the root of the project.
5. Build the image:

```
docker compose build
```

6. Run the containers to create the Database:

```
docker compose up
```

7. Stop the containers pressing Ctrl+C or:

```
docker compose down
```

8. Run the migrations:

```
docker compose run web alembic upgrade head
```

9. When you want to stop the containers, press Ctrl+C or:

```
docker compose down
```

## API Documentation

1. Run the containers

```
docker compose up
```

2. Access:

- Swagger: http://localhost:8000/api/v1/docs
- Redoc: http://localhost:8000/api/v1/redoc

## Run Tests

```
docker compose run web pytest
```

## Run Tests with Coverage

1. Run tests with [Pytest](https://docs.pytest.org/en/7.1.x/contents.html).

```
docker compose run web coverage run -m pytest
```

2. To check the test coverage, it is possible to use Terminal Report or HTML.

### Terminal Report

3. Run:

```
docker compose run web coverage report
```

![image](https://github.com/marcelloinfante/happy-scribe-api/assets/80683232/9fc5a849-2cea-42e4-8797-17c4ead8a568)

### HTML

3. Run:

```
docker compose run web coverage html
```

4. Initialize the `/htmlcov` directory generated by the test coverage using the [Live-Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension in VSCode.
5. Go to http://localhost:5500/htmlcov/
6. Check the test coverage via HTML:

![image](https://github.com/marcelloinfante/happy-scribe/assets/80683232/5f0c71a3-50ac-4fe8-bf0c-ef90aedf890a)

## Delete Database

```
docker compose down -v
```

## Create migration

```
docker compose run web alembic revision --autogenerate -m “first_commit”
```

## Migrate

```
docker compose run web alembic upgrade head
```

## Downgrade

```
docker compose run web alembic downgrade base
```

## List Migrations History

```
docker compose run web alembic history
```

## Run Commands in Container terminal

```
docker compose run web COMMAND
```

## Seeds

```
docker compose run web python app/seeds.py
```
