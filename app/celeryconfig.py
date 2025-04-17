from app.config import settings

broker_url = settings.celery_broker_url
result_backend = settings.celery_result_backend
