from fastapi import APIRouter

from app.workers.task import task

router = APIRouter(prefix="/worker", tags=["worker"])


@router.post("/test")
def test():
    task.delay("TEST")
    return "Executing Task!"
