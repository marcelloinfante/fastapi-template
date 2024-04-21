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
docker compose exec web alembic upgrade head
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

## Run Tests com Coverage

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

### HTML

3. Run:

```
docker compose run web coverage html
```

5. Initialize the `/htmlcov` directory generated by the test coverage using the [Live-Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension in VSCode.
6. Go to http://localhost:5500/htmlcov/
7. Check the test coverage via HTML:

![image](https://github.com/marcelloinfante/ai-studio-api/assets/80683232/24a840f3-75dd-4645-b5f6-060aa13f4db8)

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
