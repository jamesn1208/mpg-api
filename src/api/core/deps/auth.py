import logging
from fastapi import Request, Depends
from typing import Annotated
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from sqlalchemy import select

from api.core.models import Users
from api.core.exceptions import NoAuth, Unauthenticated


def get_user_id(request: Request) -> int:
    try:
        auth_token = request.cookies['X-Auth-Token']
        with request.app.state.database() as session:
            return session.execute(select(Users.id).where(Users.session_token == auth_token)).scalar_one()

    except NoResultFound as e:
        raise Unauthenticated from e
    except SQLAlchemyError:
        logging.exception("Failed whilst interacting with database session.")
        raise
    except KeyError as e:
        # No auth cookie found
        raise NoAuth from e


type USER_ID = Annotated[int, Depends(get_user_id)]
