from celery import Celery

app = Celery(
    "app",
    include=[
        "app.workers.task",
    ],
)

app.config_from_object("app.celeryconfig")
