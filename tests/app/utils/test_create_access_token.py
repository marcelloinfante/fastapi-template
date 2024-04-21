import pytest

from app.utils.create_access_token import create_access_token
from app.utils.decode_access_token import decode_access_token


def test_create_access_token():
    access_token = create_access_token(1)
    payload = decode_access_token(access_token)

    assert isinstance(access_token, str)
    assert isinstance(payload, dict)
    assert payload.get("sub") == "1"
    assert payload.get("exp")
