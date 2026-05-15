from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, IntegrityError

from api.core.models import Users
from api.core.exceptions import UnknownAccount, UsernameTaken


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


def remove_session_token(user_id: int, session: Session) -> None:
    """
    Remove the session token from a given user.

    :param user_id: The user_id to remove the session for.
    :param session: The database session to use.
    :return: Nothing.
    """
    try:
        user = session.execute(select(Users).where(Users.id == user_id)).scalar_one()  # type: ignore
        user.session_token = None
        session.flush()
    except NoResultFound as e:
        raise UnknownAccount from e


def delete_user(user_id: int, session: Session) -> None:
    """
    Remove a given user from Users table.

    :param user_id: The user_id to remove.
    :param session: The database session to use.
    :return: Nothing.
    """
    try:
        user = session.execute(select(Users).where(Users.id == user_id)).scalar_one()  # type: ignore
        session.delete(user)
        session.flush()
    except NoResultFound as e:
        raise UnknownAccount from e


def update_user_password(user_id: int, new_password_hash: str, session: Session) -> None:
    """
    Update a user's password hash in the Users table.

    :param user_id: user_id to update.
    :param new_password_hash: New password hash to use.
    :param session: Database session to use
    :return: Nothing.
    """
    try:
        user = session.execute(select(Users).where(Users.id == user_id)).scalar_one()  # type: ignore
        user.hash = new_password_hash
        session.flush()
    except NoResultFound as e:
        raise UnknownAccount from e


def update_user_username(user_id: int, new_username: str, session: Session) -> None:
    """
    Update a user's password hash in the Users table.

    :param user_id: user_id to update.
    :param new_username: New username to use.
    :param session: Database session to use
    :return: Nothing.
    """
    try:
        user = session.execute(select(Users).where(Users.id == user_id)).scalar_one()  # type: ignore
        user.name = new_username
        session.flush()
    except IntegrityError as e:
        raise UsernameTaken from e
    except NoResultFound as e:
        raise UnknownAccount from e
