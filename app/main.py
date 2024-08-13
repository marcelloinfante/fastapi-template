from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqladmin import Admin

from app.api.v1.main import app as v1

from app.db import engine
from app.config import settings

from app.admin.auth import AdminAuth
from app.admin.user import UserAdmin
from app.admin.plan import PlanAdmin


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck", status_code=200)
def healthcheck():
    pass


app.mount("/api/v1", v1)


authentication_backend = AdminAuth(secret_key=settings.admin_secret_key)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(PlanAdmin)
