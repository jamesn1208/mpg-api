from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from uuid import uuid4
from asyncio import to_thread

from . import schemas, models
from api.core.exceptions import UsernameTaken


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

    # Respond
    return schemas.User(id=db_user.id,
                        username=db_user.name,
                        token=db_user.session_token)
