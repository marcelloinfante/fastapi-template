from sqlmodel import Session
from fastapi.testclient import TestClient

from tests.factories.user import UserFactory

from app.models.user import UserRead

from app.utils.create_access_token import create_access_token


def test_get_current_user(client: TestClient, session: Session):
    user = UserFactory().create(session)

    access_token = create_access_token(user.id)

    response = client.get("/user", headers={"Authorization": f"Bearer {access_token}"})

    assert response.status_code == 200
    assert UserRead(**response.json())


def test_get_current_user_without_token(client: TestClient):
    response = client.get("/user")

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
