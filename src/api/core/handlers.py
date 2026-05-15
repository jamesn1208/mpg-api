from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from argon2.exceptions import VerifyMismatchError

from api.core.exceptions import UsernameTaken, UnknownAccount


def register(app: FastAPI) -> None:
    app.add_exception_handler(NotImplementedError, handle_not_implemented_exception)
    app.add_exception_handler(SQLAlchemyError, handle_sql_alchemy_error)
    app.add_exception_handler(UsernameTaken, handle_username_taken)
    app.add_exception_handler(UnknownAccount, handle_unknown_account)
    app.add_exception_handler(VerifyMismatchError, handle_invalid_password)


async def handle_not_implemented_exception(request: Request, exc: NotImplementedError) -> JSONResponse:
    return JSONResponse(
        status_code=501,
        content={"detail": "This feature is not implemented yet."},
    )


async def handle_username_taken(request: Request, exc: UsernameTaken) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": "This username is already taken."},
    )


def handle_invalid_password(request: Request, exc: UsernameTaken) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"detail": "Unknown username or password."},
    )


async def handle_unknown_account(request: Request, exc: UnknownAccount) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": "This username is not known by our service."},
    )


async def handle_sql_alchemy_error(request: Request, exc: SQLAlchemyError) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"detail": "Failed whilst interacting with the database."},
    )
