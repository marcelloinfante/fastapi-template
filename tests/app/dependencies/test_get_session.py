from app.dependencies.get_session import get_session


def test_get_session():
    session = get_session()
    assert session
