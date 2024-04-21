from datetime import datetime, timedelta
from jose import jwt

from app.config import settings


def create_access_token(
    id: str, expire_minutes: int = settings.access_token_expire_minutes
) -> str:
    to_encode = {"sub": str(id)}

    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)

    to_encode.update({"exp": expire})
    access_token = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.hash_algorithm
    )

    return access_token
