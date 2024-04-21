from app.dependencies.get_session import get_session
from sqlmodel import Session


def test_get_session():
    for session in get_session():
        assert isinstance(session, Session)
