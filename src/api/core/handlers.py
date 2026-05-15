from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from argon2.exceptions import VerifyMismatchError

from api.core.exceptions import UsernameTaken, UnknownAccount, NoAuth, Unauthenticated


def register(app: FastAPI) -> None:
    app.add_exception_handler(NotImplementedError, handle_not_implemented_exception)
    app.add_exception_handler(SQLAlchemyError, handle_sql_alchemy_error)
    app.add_exception_handler(UsernameTaken, handle_username_taken)
    app.add_exception_handler(UnknownAccount, handle_unknown_account)
    app.add_exception_handler(VerifyMismatchError, handle_invalid_password)
    app.add_exception_handler(NoAuth, handle_no_auth)
    app.add_exception_handler(Unauthenticated, handle_unauthenticated)


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


def handle_unauthenticated(request: Request, exc: Unauthenticated) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"detail": "Could not authenticate with provided token."},
    )


def handle_no_auth(request: Request, exc: NoAuth) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"detail": "No auth cookie present in request."},
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
