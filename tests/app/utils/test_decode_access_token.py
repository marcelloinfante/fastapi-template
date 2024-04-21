import pytest

from app.utils.decode_access_token import decode_access_token
from app.utils.create_access_token import create_access_token


def test_decode_access_token():
    access_token = create_access_token(1)
    payload = decode_access_token(access_token)

    assert isinstance(payload, dict)
    assert payload["sub"] == "1"
    assert payload["exp"]


def test_decode_access_token_with_invalid_token():
    with pytest.raises(Exception):
        decode_access_token("invalid token")


def test_decode_access_token_with_integer():
    with pytest.raises(Exception):
        decode_access_token(0)
