from passlib.context import CryptContext


def encrypt_password(password: str) -> str:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)
