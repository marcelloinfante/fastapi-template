from sqlmodel import Session, select
from fastapi.testclient import TestClient

from tests.factories.user import UserFactory

from app.models.user import User, UserSession


def test_register(client: TestClient, session: Session):
    user = UserFactory()
    response = client.post("/auth/register", json=user.model_dump(by_alias=True))

    statement = select(User).where(User.email == user.email)
    result = session.exec(statement)

    user_db = result.one()

    assert user_db
    assert user_db.email == user.email

    assert response.status_code == 201

    assert UserSession(**response.json())


def test_register_duplicated_email(client: TestClient, session: Session):
    user = UserFactory()
    user.create(session)

    response = client.post("/auth/register", json=user.model_dump(by_alias=True))

    assert response.status_code == 400
    assert response.json()["detail"] == "Data invalid"


def test_register_without_email(client: TestClient):
    user = UserFactory(email=None)

    response = client.post("/auth/register", json=user.model_dump(by_alias=True))

    assert response.status_code == 422


def test_register_without_first_name(client: TestClient):
    user = UserFactory(first_name=None)

    response = client.post("/auth/register", json=user.model_dump(by_alias=True))

    assert response.status_code == 422


def test_register_without_last_name(client: TestClient):
    user = UserFactory(last_name=None)

    response = client.post("/auth/register", json=user.model_dump(by_alias=True))

    assert response.status_code == 422


def test_register_without_password(client: TestClient):
    user = UserFactory(password=None)

    response = client.post("/auth/register", json=user.model_dump(by_alias=True))

    assert response.status_code == 422
