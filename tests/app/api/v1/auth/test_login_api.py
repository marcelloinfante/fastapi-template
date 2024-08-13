from sqlmodel import Session
from fastapi.testclient import TestClient

from tests.factories.user import UserFactory
from tests.factories.plan import PlanFactory

from app.models.user import UserSession


def test_login(client: TestClient, session: Session):
    user_factory = UserFactory()
    user = user_factory.create(session)

    plan_factory = PlanFactory(user_id=user.id)
    plan_factory.create(session=session)

    response = client.post(
        "/auth/login",
        data={
            "username": user_factory.email,
            "password": user_factory.password,
        },
    )

    assert response.status_code == 200
    assert UserSession(**response.json())


def test_login_user_do_not_exists(client: TestClient):
    user = UserFactory()

    response = client.post(
        "/auth/login",
        data={
            "username": user.email,
            "password": user.password,
        },
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_login_wrong_password(client: TestClient, session: Session):
    user = UserFactory()
    user.create(session)

    response = client.post(
        "/auth/login",
        data={
            "username": user.email,
            "password": "wrong password",
        },
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_login_user_with_empty_username(client: TestClient):
    user = UserFactory()

    response = client.post(
        "/auth/login",
        data={
            "username": None,
            "password": user.password,
        },
    )

    assert response.status_code == 422


def test_login_user_with_empty_password(client: TestClient):
    user = UserFactory()

    response = client.post(
        "/auth/login",
        data={
            "username": user.email,
            "password": None,
        },
    )

    assert response.status_code == 422
