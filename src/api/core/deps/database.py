import logging

from fastapi import Request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


def get_session(request: Request) -> Session:
    try:
        with request.app.state.database() as session:
            yield session
    except SQLAlchemyError:
        logging.exception("Failed whilst interacting with database session.")
        raise
