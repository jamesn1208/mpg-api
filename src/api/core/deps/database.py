import logging

from fastapi import Request, Depends
from typing import Annotated
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


def get_session(request: Request) -> Session:
    try:
        with request.app.state.database() as session:
            yield session
            session.commit()
    except SQLAlchemyError:
        logging.exception("Failed whilst interacting with database session.")
        raise


type DB_SESSION = Annotated[Session, Depends(get_session)]
