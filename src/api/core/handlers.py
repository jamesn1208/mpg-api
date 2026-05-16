from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from argon2.exceptions import VerifyMismatchError

from api.core.exceptions import UsernameTaken, UnknownAccount, NoAuth, Unauthenticated, NoAction, ActionError


def register(app: FastAPI) -> None:
    app.add_exception_handler(NotImplementedError, handle_not_implemented_exception)
    app.add_exception_handler(SQLAlchemyError, handle_sql_alchemy_error)
    app.add_exception_handler(UsernameTaken, handle_username_taken)
    app.add_exception_handler(UnknownAccount, handle_unknown_account)
    app.add_exception_handler(VerifyMismatchError, handle_invalid_password)
    app.add_exception_handler(NoAuth, handle_no_auth)
    app.add_exception_handler(Unauthenticated, handle_unauthenticated)
    app.add_exception_handler(NoAction, handle_no_action)
    app.add_exception_handler(ActionError, handle_action_error)


async def handle_not_implemented_exception(request: Request, exc: NotImplementedError) -> JSONResponse:
    return JSONResponse(
        status_code=501,
        content={"message": "This feature is not implemented yet.",
                 "status": False},
    )


async def handle_action_error(request: Request, exc: ActionError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc),
                 "status": False},
    )


async def handle_username_taken(request: Request, exc: UsernameTaken) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"message": "This username is already taken.",
                 "status": False},
    )


async def handle_no_action(request: Request, exc: NoAction) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"message": "No action to be performed.",
                 "status": False},
    )


def handle_invalid_password(request: Request, exc: UsernameTaken) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"message": "Unknown username or password.",
                 "status": False},
    )


def handle_unauthenticated(request: Request, exc: Unauthenticated) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"message": "Could not authenticate with provided token.",
                 "status": False},
    )


def handle_no_auth(request: Request, exc: NoAuth) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"message": "No auth cookie present in request.",
                 "status": False},
    )


async def handle_unknown_account(request: Request, exc: UnknownAccount) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"message": "This username is not known by our service.",
                 "status": False},
    )


async def handle_sql_alchemy_error(request: Request, exc: SQLAlchemyError) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"message": "Failed whilst interacting with the database.",
                 "status": False},
    )
