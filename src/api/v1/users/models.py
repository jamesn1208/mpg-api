from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from api.core.models import Users
from api.core.exceptions import UnknownAccount


def does_username_exist(username: str, session: Session) -> bool:
    return session.execute(select(Users).where(Users.name == username)).scalar() is not None


def create_user(username: str, hashed_password: str, token: str, session: Session) -> int:
    user = Users(name=username,
                 hash=hashed_password,
                 session_token=token)
    session.add(user)
    session.flush()
    session.refresh(user)

    return user.id


def get_user_by_username(username: str, session: Session) -> Users:
    try:
        return session.execute(select(Users).where(Users.name == username)).scalar_one()
    except NoResultFound as e:
        raise UnknownAccount from e
