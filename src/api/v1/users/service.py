from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from uuid import uuid4
from asyncio import to_thread

from . import schemas, models
from api.core.exceptions import UsernameTaken, NoAction
from api.core.schemas import ActionResponse


async def create_user(user: schemas.UserAuth, session: Session) -> schemas.User:
    # Check the username is not already taken
    if await to_thread(models.does_username_exist,
                       username=user.username,
                       session=session):
        raise UsernameTaken()

    # Creation dependencies
    ph = PasswordHasher()

    # Get values
    hashed_password = ph.hash(user.password)
    token = str(uuid4())
    user_id = await to_thread(models.create_user,
                              username=user.username,
                              hashed_password=hashed_password,
                              token=token,
                              session=session)

    # Respond
    return schemas.User(id=user_id,
                        username=user.username,
                        token=token)


async def login(user: schemas.UserAuth, session: Session) -> schemas.User:
    # Get values
    db_user = await to_thread(models.get_user_by_username,
                              username=user.username,
                              session=session)

    # Login dependencies
    ph = PasswordHasher()

    # Check the password is correct
    ph.verify(hash=db_user.hash,
              password=user.password)

    # Check if we have a session token already
    if db_user.session_token is None:
        # Generate a new token
        token = str(uuid4())
        db_user.session_token = token
        session.flush()

    # Respond
    return schemas.User(id=db_user.id,
                        username=db_user.name,
                        token=db_user.session_token)


async def logout(user_id: int, session: Session) -> ActionResponse:
    # Remove session token
    await to_thread(models.remove_session_token,
                    user_id=user_id,
                    session=session)

    # Respond
    return ActionResponse(success=True,
                          message="Successfully logged out.")


async def delete_user(user_id: int, session: Session) -> ActionResponse:
    # Remove user from database
    await to_thread(models.delete_user,
                    user_id=user_id,
                    session=session)

    # Respond
    return ActionResponse(success=True,
                          message="Successfully deleted user.")


async def update_user(user_id: int, user: schemas.UserUpdate, session: Session) -> ActionResponse:
    # Check at least one field is being updated
    if user.username is None and user.password is None:
        raise NoAction()

    if user.username is not None:
        # Update username
        await to_thread(models.update_user_username,
                        user_id=user_id,
                        new_username=user.username,
                        session=session)

    if user.password is not None:
        # Update password hash
        ph = PasswordHasher()

        hashed_password = ph.hash(user.password)
        await to_thread(models.update_user_password,
                        user_id=user_id,
                        new_password_hash=hashed_password,
                        session=session)

    # Respond
    return ActionResponse(success=True,
                          message="Successfully updated user.")
