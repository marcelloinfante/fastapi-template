from sqlmodel import Session
from fastapi.testclient import TestClient

from tests.factories.user import UserFactory

from app.models.user import User
from app.utils.create_access_token import create_access_token


def test_delete_current_user(client: TestClient, session: Session):
    created_user = UserFactory().create(session)

    access_token = create_access_token(created_user.id)

    response = client.delete(
        "/user", headers={"Authorization": f"Bearer {access_token}"}
    )

    user = session.get(User, created_user.id)

    assert user == None

    assert response.status_code == 200


def test_delete_user_without_token(client: TestClient):
    response = client.delete("/user")

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
