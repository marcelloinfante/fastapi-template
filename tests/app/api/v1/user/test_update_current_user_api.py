from sqlmodel import Session
from fastapi.testclient import TestClient

from tests.factories.user import UserFactory
from tests.factories.plan import PlanFactory

from app.models.user import UserRead
from app.utils.create_access_token import create_access_token


def test_update_current_user(client: TestClient, session: Session):
    user = UserFactory().create(session)

    plan_factory = PlanFactory(user_id=user.id)
    plan_factory.create(session=session)

    access_token = create_access_token(user.id)

    response = client.put(
        "/user",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"firstName": "new_first_name", "lastName": "new_last_name"},
    )

    assert response.status_code == 200
    assert response.json()["firstName"] == "new_first_name"
    assert response.json()["lastName"] == "new_last_name"


def test_update_current_user_email(client: TestClient, session: Session):
    user = UserFactory().create(session)

    plan_factory = PlanFactory(user_id=user.id)
    plan_factory.create(session=session)

    access_token = create_access_token(user.id)

    response = client.put(
        "/user",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"email": "new@email.com"},
    )

    assert response.status_code == 200
    assert response.json()["email"] == user.email


def test_update_current_user_without_token(client: TestClient):
    response = client.put("/user", json={"first_name": "new_first_name"})

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}


def test_update_current_user_without_payload(client: TestClient, session: Session):
    user = UserFactory().create(session)

    plan_factory = PlanFactory(user_id=user.id)
    plan_factory.create(session=session)

    access_token = create_access_token(user.id)

    response = client.put(
        "/user",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 422


def test_update_current_empty_payload(client: TestClient, session: Session):
    user = UserFactory().create(session)

    plan_factory = PlanFactory(user_id=user.id)
    plan_factory.create(session=session)

    access_token = create_access_token(user.id)

    response = client.put(
        "/user",
        headers={"Authorization": f"Bearer {access_token}"},
        json={},
    )

    assert response.status_code == 200
    assert UserRead.model_validate(response.json()) == UserRead.model_validate(user)
