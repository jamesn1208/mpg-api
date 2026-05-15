from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register(app: FastAPI) -> None:
    app.add_exception_handler(NotImplementedError, handle_not_implemented_exception)


async def handle_not_implemented_exception(request: Request, exc: NotImplementedError) -> JSONResponse:
    return JSONResponse(
        status_code=501,
        content={"detail": "This feature is not implemented yet."},
    )
