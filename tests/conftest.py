import pytest

from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

import sqlalchemy_utils

from app.api.v1.main import app
from app.dependencies.get_session import get_session


@pytest.fixture(scope="function")
def session():
    engine = create_engine("postgresql://fastapi:fastapi@db:5432/test_db")

    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)

    SQLModel.metadata.create_all(bind=engine)

    with Session(engine) as session:
        yield session

    sqlalchemy_utils.drop_database(engine.url)


@pytest.fixture(scope="function")
def client(session: Session):
    app.dependency_overrides[get_session] = lambda: session

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
