from app.celery import app


@app.task(name="task")
def task(text):
    return text[::-1]
