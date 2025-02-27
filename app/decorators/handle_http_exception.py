import traceback

from fastapi import HTTPException, status


def handle_http_exception(func):
    def wrapper(cls, *args, **kwargs):
        try:
            res = func(cls, *args, **kwargs)

        except HTTPException as http_ex:
            raise http_ex

        except Exception as e:
            traceback.print_exc()

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Data invalid",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return res

    return wrapper
