from jose import jwt
from app.config import settings


def decode_access_token(access_token: str) -> dict:
    return jwt.decode(
        access_token, settings.secret_key, algorithms=[settings.hash_algorithm]
    )
