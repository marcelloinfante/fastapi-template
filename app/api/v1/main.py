from fastapi import FastAPI

from app.api.v1 import auth
from app.api.v1 import user


app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
