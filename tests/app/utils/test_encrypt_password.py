import pytest

from app.utils.encrypt_password import encrypt_password


def test_encrypt_password():
    password = "password"
    encrypted_password = encrypt_password(password)

    assert isinstance(encrypted_password, str)
    assert encrypted_password != password


def test_encrypt_password_without_password():
    with pytest.raises(TypeError) as e:
        encrypt_password(None)

    assert str(e.value) == "secret must be unicode or bytes, not None"
