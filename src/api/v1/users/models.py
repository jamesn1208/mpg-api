from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from api.core.models import Users
from api.core.exceptions import UnknownAccount


def does_username_exist(username: str, session: Session) -> bool:
    """
    Checks if a given username exists in the Users table.

    :param username: Username to check.
    :param session: Session to check with.
    :return: (bool) True if username exists, else False.
    """
    return session.execute(select(Users).where(Users.name == username)).scalar() is not None  # type: ignore


def create_user(username: str, hashed_password: str, token: str, session: Session) -> int:
    """
    Adds provided username, password & token to the Users table, and returns the ID of the new user.

    :param username: The username of the new user.
    :param hashed_password: The hashed password of the new user (argon2id).
    :param token: The session token for the new user.
    :param session: The database session to use.
    :return: (int) The ID of the new user.
    """
    user = Users(name=username,
                 hash=hashed_password,
                 session_token=token)
    session.add(user)
    session.flush()
    session.refresh(user)

    return user.id


def get_user_by_username(username: str, session: Session) -> Users:
    """
    Get an instance of the Users model by username.

    :param username: The username to get info about.
    :param session: The database session to use.
    :return: An instance of the Users model.
    """
    try:
        return session.execute(select(Users).where(Users.name == username)).scalar_one()  # type: ignore
    except NoResultFound as e:
        raise UnknownAccount from e
